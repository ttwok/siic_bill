import pandas as pd
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_website(user_id, password, status_text, df):
    # Chrome 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option("detach", True)  # 브라우저가 자동으로 닫히지 않도록 설정

    # WebDriver 초기화
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 웹페이지로 이동
        driver.get('https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php')

        # 로그인 정보 입력 및 로그인 버튼 클릭
        wait = WebDriverWait(driver, 10)

        id_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="adm_id"]')))
        id_input.send_keys(user_id)

        password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="adm_pw"]')))
        password_input.send_keys(password)

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btnLogin"]/span')))
        login_button.click()

        status_text.text("로그인 시도 중...")

        # 로그인 성공 여부 확인
        WebDriverWait(driver, 10).until(EC.url_changes('https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php'))
        status_text.text("로그인 성공")

        # 로그인 성공 후 청구서 발행/관리 페이지로 이동
        driver.get('https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php')
        status_text.text("청구서 발행/관리 페이지로 이동 중...")

        # 청구서 발행/관리 페이지에 접근
        link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php"]')))
        link.click()
        status_text.text("청구서 발행/관리 페이지 접근 완료")

        # 자동화 작업 실행
        original_window = driver.current_window_handle
        for index, row in df.iterrows():
            status_text.text(f"{row['쇼핑몰명']} 자동화 진행 중...")
            result = perform_automation(driver, row, status_text, original_window)
            st.write(f"{row['쇼핑몰명']}: {'ok' if result else 'ok'}")
            time.sleep(2)  # 각 작업 사이에 2초 대기

            # 작업 완료 후 원래 창으로 돌아가기
            driver.switch_to.window(original_window)

            # 다시 청구서 발행/관리 페이지로 이동
            driver.get('https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php')

        return True
    except Exception as e:
        status_text.text(f"로그인 실패: {e}")
        driver.quit()
        return False

def perform_automation(driver, row, status_text, original_window):
    try:
        wait = WebDriverWait(driver, 10)

        # 드롭다운 메뉴 클릭
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@name="srch_key"]')))
        dropdown.click()

        # "쇼핑몰명" 옵션 클릭
        option = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@name="srch_key"]/option[@value="mall_nm"]')))
        option.click()

        # 검색 입력란에 쇼핑몰명 입력
        search_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="srch_val"]')))
        search_input.send_keys(row['쇼핑몰명'])
        search_input.send_keys(Keys.RETURN)
        time.sleep(1)

        # 첫 번째 행의 "신규발행" 링크 클릭
        first_new_issue_link = wait.until(EC.element_to_be_clickable((By.XPATH, '(//tbody[@class="center"]//tr)[1]//a[text()="신규발행"]')))
        first_new_issue_link.click()

        # 새 창으로 전환
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in driver.window_handles if window != original_window][0]
        driver.switch_to.window(new_window)

        # 신규 발행 화면의 요소들이 로드될 때까지 대기
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="svc_price1"]')))

        # I/B 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="svc_price1"]')
        price_input.send_keys(row['콜단가'])

        num_input = driver.find_element(By.XPATH, '//input[@id="svc_num1"]')
        num_input.send_keys(row['I/B:건수'])

        # O/B 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="svc_price2"]')
        price_input.send_keys(row['콜단가'])

        num_input = driver.find_element(By.XPATH, '//input[@id="svc_num2"]')
        num_input.send_keys(row['O/B:건수'])

        # 10초 이하 단선 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="svc_price3"]')
        price_input.send_keys(row['콜단가'])

        num_input = driver.find_element(By.XPATH, '//input[@id="svc_num3"]')
        num_input.send_keys(row['10초이하건수'])

        # 게시판 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="svc_price4"]')
        price_input.send_keys(row['게시판단가'])

        num_input = driver.find_element(By.XPATH, '//input[@id="svc_num4"]')
        num_input.send_keys(row['게시판단가'])

        # 상담톡 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="svc_price5"]')
        price_input.send_keys(row['상담톡단가'])

        num_input = driver.find_element(By.XPATH, '//input[@id="svc_num5"]')
        num_input.send_keys(row['상담톡단가'])

        # 기본운영비 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="rec_basic"]')
        price_input.clear()  # 기존 값을 지움
        price_input.send_keys(row['기본운영비'])

        # 착신번호 기본료 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="tel_rec_price"]')
        price_input.send_keys(row['착신기본료'])

        # 발신 통신료 입력란에 값 입력
        price_input = driver.find_element(By.XPATH, '//input[@id="tel_send_price"]')
        price_input.send_keys(row['발신통신료'])

        # 자동계산 버튼 클릭
        calculate_button = driver.find_element(By.XPATH, '//a[@class="btnCtrl"]/span[text()="자동계산"]')
        calculate_button.click()
        status_text.text("자동계산 버튼 클릭 완료")

        # 발행 버튼 클릭
        issue_button = driver.find_element(By.XPATH, '//button[@class="btnSubmit"]/span[text()="발행"]')
        issue_button.click()
        status_text.text("발행 버튼 클릭 완료")

        # 팝업창 대기 및 전환
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        status_text.text("팝업창 확인 클릭 완료")

        # 팝업창의 특정 텍스트를 포함한 버튼 클릭
        popup_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "확인")]')))
        popup_button.click()
        status_text.text("팝업창의 특정 텍스트를 포함한 버튼 클릭 완료")

        # "청구서가 발행되었습니다." 알림 처리
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        status_text.text("청구서 발행 완료")

        # 작업 완료 후 새 창 닫기 및 원래 창으로 전환
        driver.close()
        driver.switch_to.window(original_window)

        return True
    except Exception as e:
        status_text.text(f"예외 발생: {e}")
        return False

# Streamlit 앱 설정
st.title('정산서 업로드 자동화')

# 파일 업로드 위젯
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded_file is not None:
    # 업로드된 파일을 데이터프레임으로 읽기
    df = pd.read_excel(uploaded_file)
    
    # 데이터프레임 표시
    st.write("업로드된 데이터:")
    st.dataframe(df)
    
    # 로그인 정보 입력 받기
    st.sidebar.header('로그인 정보')
    user_id = st.sidebar.text_input('아이디', 'dwcha')
    password = st.sidebar.text_input('비밀번호', 'cafe24@002', type='password')

    # 로그인 버튼
    if st.sidebar.button('로그인'):
        status_text = st.sidebar.empty()
        status_text.text("로그인 시도 중...")
        login_to_website(user_id, password, status_text, df)
else:
    st.warning("엑셀 파일을 업로드해주세요.")
