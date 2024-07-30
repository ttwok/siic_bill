import streamlit as st

# wide 화면 레이아웃 설정
st.set_page_config(layout="wide")

st.title("Embed a Website in Streamlit - Wide Screen")

# 특정 사이트 URL
url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

# wide 화면에 맞춰 아이프레임 생성
st.components.v1.iframe(src=url, width=1400, height=800)
