import streamlit as st

st.set_page_config(layout="wide")
st.title("Embed a Website in Streamlit")

# 특정 사이트 URL
url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

# 아이프레임 생성
st.components.v1.iframe(src=url, width=1000, height=800)
st.components.v1.iframe(src=url, width=1000, height=800)
