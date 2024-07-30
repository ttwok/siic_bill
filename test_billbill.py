import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    st.title('Web Scraping with BeautifulSoup')
    st.write('Enter a URL to scrape.')

    url = st.text_input('URL', 'https://www.google.com')

    if st.button('Scrape'):
        try:
            # Get the HTML content of the page
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            html_content = response.text

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Display the page title
            page_title = soup.title.string
            st.write(f'Page Title: {page_title}')

            # Display a preview of the page content
            st.write('Page Content Preview:')
            st.write(soup.prettify()[:500])  # Display the first 500 characters of the HTML

        except requests.exceptions.RequestException as e:
            st.error(f'Error fetching the URL: {e}')

if __name__ == '__main__':
    main()
