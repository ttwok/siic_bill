import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 웹드라이버 설정
@st.experimental_singleton
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

driver = get_driver()

st.title("Streamlit Web Automation Example")

if st.button("Connect to Naver"):
    driver.get("https://www.naver.com")
    title = driver.title
    st.write(f"Title of the page is: {title}")

    # 예시: 특정 엘리먼트를 찾고 작업 수행
    element = driver.find_element(By.TAG_NAME, "h1")
    st.write(f"H1 tag text is: {element.text}" if element else "No H1 tag found.")
