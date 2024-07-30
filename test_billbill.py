import streamlit as st

st.title("Embed a Website in Streamlit")

# 특정 사이트 URL
url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

# 아이프레임 생성
st.components.v1.iframe(src=url, width=800, height=600)
