import streamlit as st
import asyncio
from pyppeteer import launch

async def get_page_title(url):
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page.goto(url)
    title = await page.title()
    await browser.close()
    return title

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
