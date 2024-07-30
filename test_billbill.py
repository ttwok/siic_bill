import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("Login and Display Content in Streamlit")

# 로그인 정보를 입력 받습니다
st.sidebar.header("Login Information")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

if login_button:
    login_url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

    # 로그인 데이터
    login_data = {
        'username_field_name': username,  # 실제 필드 이름으로 변경
        'password_field_name': password,  # 실제 필드 이름으로 변경
    }

    # 세션 생성
    session = requests.Session()

    # 로그인 요청 보내기
    response = session.post(login_url, data=login_data)

    # 로그인 성공 여부 확인
    if "로그인 실패 메시지" in response.text:  # 실제 로그인 실패 메시지로 변경
        st.error("Invalid username or password")
    else:
        st.success("Login successful")
        
        # 로그인 성공 후 페이지를 iframe으로 표시
        st.components.v1.iframe(src=login_url, width=1400, height=800)
