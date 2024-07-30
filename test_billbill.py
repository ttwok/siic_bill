import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

st.set_page_config(layout="wide")
st.title("Login and Display Content in Streamlit")

# 로그인 정보를 입력 받습니다
st.sidebar.header("Login Information")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

if login_button:
    # Selenium을 사용하여 브라우저를 실행하고 로그인합니다
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 브라우저 창을 표시하지 않음
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 로그인 페이지로 이동합니다
        driver.get("https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php")

        # 로그인 정보를 입력하고 로그인 버튼을 클릭합니다
        driver.find_element(By.NAME, 'username_field_name').send_keys(username)  # 'username_field_name'을 실제 필드 이름으로 변경
        driver.find_element(By.NAME, 'password_field_name').send_keys(password)  # 'password_field_name'을 실제 필드 이름으로 변경
        driver.find_element(By.NAME, 'password_field_name').send_keys(Keys.RETURN)

        # 로그인 후 페이지 로드 대기
        time.sleep(3)

        # 로그인 후 페이지의 HTML을 가져옵니다
        page_html = driver.page_source

        # HTML을 Streamlit에 표시합니다
        st.components.v1.html(page_html, width=1400, height=800)

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        driver.quit()
