import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("Embed a Website in Streamlit")

url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

response = requests.get(url)
if response.status_code == 200:
    st.components.v1.html(response.text, width=1400, height=800)
else:
    st.error("Failed to load the page")
