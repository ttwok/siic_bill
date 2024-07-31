import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("Login and Display Content in Streamlit")

# 세션 상태를 초기화
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'cookies' not in st.session_state:
    st.session_state.cookies = None

def login(username, password):
    login_url = "https://siic-admin-local.cafe24.com/admin/login"  # 로그인 API URL
    login_data = {
        'username': username,
        'password': password,
    }
    session = requests.Session()
    response = session.post(login_url, data=login_data)
    
    if response.status_code == 200:
        st.session_state.logged_in = True
        st.session_state.cookies = session.cookies.get_dict()
        return True
    else:
        return False

def display_iframe(url):
    cookies = st.session_state.cookies
    iframe_html = f"""
    <iframe src="{url}" width="1400" height="800" sandbox="allow-same-origin allow-scripts allow-forms"></iframe>
    <script>
    document.cookie = "{'; '.join([f'{key}={value}' for key, value in cookies.items()])}";
    </script>
    """
    st.components.v1.html(iframe_html, width=1400, height=800)

if not st.session_state.logged_in:
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")

    if login_button:
        if login(username, password):
            st.success("Login successful")
        else:
            st.error("Invalid username or password")
else:
    st.success("You are logged in")
    url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"
    display_iframe(url)
