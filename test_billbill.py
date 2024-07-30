import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, request, jsonify
import threading
import time
import requests

# Create Flask app
app = Flask(__name__)

@app.route('/automate_login', methods=['POST'])
def automate_login():
    data = request.json
    user_id = data['user_id']
    password = data['password']
    login_url = data['login_url']

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(login_url)
    wait = WebDriverWait(driver, 10)

    # 아이디 입력
    id_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="adm_id"]')))
    id_input.send_keys(user_id)

    # 비밀번호 입력
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="adm_pw"]')))
    password_input.send_keys(password)

    # 로그인 버튼 클릭
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btnLogin"]/span')))
    login_button.click()

    time.sleep(5)  # 로그인 후 대기
    driver.quit()

    return jsonify({"status": "success"})

# Run Flask app in a separate thread
def run_flask():
    app.run(host='0.0.0.0', port=5000)

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Streamlit app
st.title("Automated Login to Cafe24")

user_id = "dwcha"
password = "cafe24@002"
login_url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"
backend_url = "http://localhost:5000/automate_login"

def automate_login(user_id, password, login_url):
    try:
        response = requests.post(backend_url, json={
            'user_id': user_id,
            'password': password,
            'login_url': login_url
        })
        response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킴
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return {"status": "error"}

if st.button("Login to Cafe24"):
    result = automate_login(user_id, password, login_url)
    if result.get("status") == "success":
        st.success("Login process completed.")
    else:
        st.error("Login failed.")
