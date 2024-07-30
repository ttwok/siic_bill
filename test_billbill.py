import streamlit as st
import httpx
from bs4 import BeautifulSoup
import asyncio

async def get_page_title(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else 'No title found'

def get_title(url):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    title = loop.run_until_complete(get_page_title(url))
    loop.close()
    return title

st.title("Streamlit Web Automation Example")

if st.button("Connect to Naver"):
    with st.spinner("Connecting to Naver..."):
        title = get_title("https://www.naver.com")
        st.write(f"Title of the page is: {title}")
