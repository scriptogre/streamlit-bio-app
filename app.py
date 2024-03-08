import streamlit as st
from utils import ncbi_text_search, fetch_titles, generate_description, generate_image


def main():
    st.title("Streamlit Biology Application")

    query = st.text_input("Enter search term:", "")

    if query:
        with st.spinner("Searching..."):
            id_list = ncbi_text_search(query)
            if id_list:
                titles = fetch_titles(id_list)
                if titles:
                    selected_title = st.selectbox("Select a result:", titles)
                    st.write("You selected:", selected_title)

                    # Generate an image based on the selected title
                    if st.button('Analyze species'):
                        with st.spinner("Generating image..."):
                            image_url = generate_image(selected_title)
                            st.image(image_url, caption=selected_title)

                        with st.spinner("Generating description..."):
                            description = generate_description(selected_title)
                            st.write(description)
            else:
                st.write("No results found.")

if __name__ == "__main__":
    main()
