import streamlit as st

st.title("Streamlit Web Automation Example")

url = "https://www.naver.com"

if st.button("Connect to Naver"):
    js = f"window.open('{url}');"
    st.write(f'<script>{js}</script>', unsafe_allow_html=True)
    st.write(f"Opening {url} in a new browser tab...")

st.markdown(f'<a href="{url}" target="_blank">Open Naver in a new tab</a>', unsafe_allow_html=True)
