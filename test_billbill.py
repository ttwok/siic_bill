import streamlit as st

st.set_page_config(layout="wide")
st.title("Embed a Website in Streamlit")

# 특정 사이트의 HTML 코드
html_content = """
<iframe src="https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php" width="1400" height="800"></iframe>
"""

st.components.v1.html(html_content, width=1400, height=800)
