# Streamlit Biology Application for iGEM Biohackathon

This repository contains a Streamlit-based application designed for the iGEM Biohackathon. It enables users to search NCBI databases, select specific search results, and generate relevant images using OpenAI's DALL-E based on the selected titles.

## Getting Started

### Prerequisites

Before running the application, ensure you have Python installed on your system. This application requires Python 3.6 or later.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/scriptogre/streamlit-bio-app.git
   ```
2. Navigate to the cloned repository directory:
   ```bash
   cd streamlit-bio-app
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

You need to create an `.env` file in the root directory of the project with the following content:

```
NCBI_API_KEY=your_ncbi_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

#### Obtaining NCBI API Key

- Go to the [NCBI Accounts](https://account.ncbi.nlm.nih.gov/) page.
- Sign in or create an account if you don't have one.
- Under the `NCBI API Key` section, click on `Create an API Key`.
- Copy the generated API key and paste it into your `.env` file as the value for `NCBI_API_KEY`.

#### Obtaining OpenAI API Key

- Visit [OpenAI](https://platform.openai.com/api-keys) and sign up or log in.
- Navigate to the API section in your account settings.
- Click on `Generate new API key`.
- Copy the generated API key and paste it into your `.env` file as the value for `OPENAI_API_KEY`.

### Running the Application

To run the Streamlit application, execute the following command in the terminal:

```bash
streamlit run app.py
```

Navigate to the URL provided by Streamlit in your browser to interact with the application.

## Contributing

Contributions to the project are welcome! Please refer to the contributing guidelines for more details.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.