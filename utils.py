import os
from dotenv import load_dotenv
import requests
from openai import OpenAI

from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Set OpenAI API key
client = OpenAI()


def ncbi_text_search(query, db="nucleotide", retmax=10):
    """Search NCBI nucleotide database for a given query."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": db,
        "term": query,
        "retmax": retmax,
        "api_key": os.getenv('NCBI_API_KEY'),
        "retmode": "json",
    }
    response = requests.get(base_url, params=params)
    if response.ok:
        idlist = response.json()["esearchresult"]["idlist"]
        return idlist
    return []


def fetch_titles(id_list, db="nucleotide"):
    """Fetch titles for a given list of IDs from NCBI."""
    if not id_list:
        return []
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": db,
        "id": ",".join(id_list),
        "api_key": os.getenv('NCBI_API_KEY'),
        "retmode": "json",
    }
    response = requests.get(base_url, params=params)
    if response.ok:
        summaries = response.json()["result"]
        titles = [summaries[id]["title"] for id in id_list if id in summaries]
        return titles
    return []


def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        quality="standard",
        size="1024x1024",
        n=1
    )
    image_url = response.data[0].url
    return image_url


def generate_description(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content