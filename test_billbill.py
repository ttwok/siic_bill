import streamlit as st
import requests

st.title("Automated Login to Cafe24")

# 로그인 정보
user_id = "dwcha"
password = "cafe24@002"
login_url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

# Flask 백엔드 서버 URL
backend_url = "http://127.0.0.1:5000/automate_login"

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
