import streamlit as st
import requests
from requests_oauthlib import OAuth2Session

st.set_page_config(layout="wide")
st.title("Google API Example")

# OAuth 2.0 클라이언트 설정
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'

# OAuth 세션 생성
google = OAuth2Session(client_id, redirect_uri='http://localhost:8501')
authorization_url, state = google.authorization_url(authorization_base_url, access_type="offline", prompt="select_account")

st.sidebar.write("Login to Google")
login_button = st.sidebar.button("Login")

if login_button:
    st.write("Please go to the following URL to authorize:")
    st.write(authorization_url)
    st.stop()

redirect_response = st.text_input("Paste the full redirect URL here:")

if redirect_response:
    google.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
    response = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
    st.write(response.json())
