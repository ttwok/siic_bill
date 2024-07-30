import streamlit as st
import requests

st.title("Automated Login to Cafe24")

# 로그인 정보
user_id = "dwcha"
password = "cafe24@002"
login_url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

backend_url = "http://<YOUR_BACKEND_SERVER_IP>:5000/automate_login"

def automate_login(user_id, password, login_url):
    response = requests.post(backend_url, json={
        'user_id': user_id,
        'password': password,
        'login_url': login_url
    })
    return response.json()

if st.button("Login to Cafe24"):
    result = automate_login(user_id, password, login_url)
    if result.get("status") == "success":
        st.success("Login process completed.")
    else:
        st.error("Login failed.")
