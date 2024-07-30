import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def perform_automation(row, status_text):
    USERNAME = 'bsuser_M3SxCe'
    ACCESS_KEY = 'y8fswxT4kr1WSSPVCNeS'
    URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    desired_cap = {
        'os': 'Windows',
        'os_version': '10',
        'browserName': 'Chrome',
        'browser_version': 'latest',
        'name': 'Streamlit Test',
        'browserstack.debug': 'true'  # 디버깅 모드 활성화
    }

    driver = webdriver.Remote(
        command_executor=URL,
        desired_capabilities=desired_cap
    )

    try:
        driver.get('https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php')

        wait = WebDriverWait(driver, 10)

        # 로그인 절차
        id_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="adm_id"]')))
        id_input.send_keys(row['아이디'])

        password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="adm_pw"]')))
        password_input.send_keys(row['비밀번호'])

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btnLogin"]/span')))
        login_button.click()

        status_text.text("로그인 시도 중...")

        # 로그인 성공 후 작업 진행
        WebDriverWait(driver, 10).until(EC.url_contains('rvn_bil_tab.php'))
        status_text.text("로그인 성공")

        # 이후 자동화 작업 코드 작성
        # ...

        driver.quit()
        return True
    except Exception as e:
        status_text.text(f"예외 발생: {e}")
        driver.quit()
        return False

st.title('정산서 업로드 자동화')

# 로그인 정보 입력 받기
st.sidebar.header('로그인 정보')
user_id = st.sidebar.text_input('아이디', 'dwcha')
password = st.sidebar.text_input('비밀번호', 'cafe24@002', type='password')

# 파일 업로드 위젯
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # 아이디와 비밀번호를 데이터프레임에 추가
    df['아이디'] = user_id
    df['비밀번호'] = password

    st.write("업로드된 데이터:")
    st.dataframe(df)

    for index, row in df.iterrows():
        status_text = st.empty()
        status_text.text(f"{row['쇼핑몰명']} 자동화 진행 중...")
        perform_automation(row, status_text)
else:
    st.warning("엑셀 파일을 업로드해주세요.")
