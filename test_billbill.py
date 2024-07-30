import streamlit as st

st.title("Streamlit Web Automation Example")

# 리디렉션할 URL 설정
url = "https://www.naver.com"

# 버튼 클릭 시 자바스크립트를 사용하여 새 탭에서 URL 열기
if st.button("Connect to Naver"):
    js = f"window.location.href = '{url}';"
    st.write(f'<script>{js}</script>', unsafe_allow_html=True)

# 링크 클릭을 통해 새 탭에서 URL 열기 (대체 방법)
st.markdown(f'<a href="{url}" target="_blank">Open Naver in a new tab</a>', unsafe_allow_html=True)
