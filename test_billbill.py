import streamlit as st
import asyncio
import nest_asyncio
from pyppeteer import launch

# nest_asyncio 적용
nest_asyncio.apply()

# pyppeteer 설정 함수
@st.cache_resource
async def get_browser():
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    return browser

async def get_page_title(url):
    browser = await get_browser()
    page = await browser.newPage()
    await page.goto(url)
    title = await page.title()
    await browser.close()
    return title

st.title("Streamlit Web Automation Example")

if st.button("Connect to Naver"):
    title = asyncio.run(get_page_title("https://www.naver.com"))
    st.write(f"Title of the page is: {title}")
