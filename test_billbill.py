import streamlit as st
import asyncio
from playwright.async_api import async_playwright

async def scrape_google():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://www.google.com')
        title = await page.title()
        await browser.close()
        return title

def main():
    st.title('Web Automation with Playwright in Streamlit')

    if st.button('Open Google and Get Title'):
        title = asyncio.run(scrape_google())
        st.write(f'Page Title: {title}')

if __name__ == '__main__':
    main()
