import streamlit as st
import webbrowser

st.title("Automated Login to Cafe24")

# 로그인 정보 입력
user_id = st.text_input("Enter your user ID", "dwcha")
password = st.text_input("Enter your password", "cafe24@002", type="password")
login_url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

# 버튼 클릭 시 URL 열기
if st.button("Open Cafe24 Login Page"):
    # 사용자가 직접 로그인하도록 안내
    webbrowser.open_new_tab(login_url)
    st.info("Opened Cafe24 login page. Please enter your login details manually.")
