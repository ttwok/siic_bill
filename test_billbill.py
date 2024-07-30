import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

st.title("Streamlit Web Automation Example")

def search_naver(query):
    # Selenium WebDriver 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 네이버 페이지 열기
    driver.get("https://www.naver.com")
    time.sleep(3)  # 페이지 로딩 대기

    # 검색어 입력 및 검색 실행
    search_box = driver.find_element(By.ID, 'query')
    search_box.send_keys(query)
    search_box.submit()

    time.sleep(3)  # 검색 결과 로딩 대기
    driver.quit()

if st.button("Connect to Naver and Search 카페24"):
    search_naver("카페24")
    st.success("Search completed and browser closed.")
