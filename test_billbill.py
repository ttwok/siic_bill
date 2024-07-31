import streamlit as st
from playwright.sync_api import sync_playwright

st.set_page_config(layout="wide")
st.title("Embed a Website in Streamlit with Playwright")

def run(playwright):
    browser = playwright.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    context = browser.new_context()
    page = context.new_page()

    # 콘솔 로그를 캡처
    page.on("console", lambda msg: print(f"Console log: {msg.text}"))
    
    # 네트워크 요청을 캡처
    page.on("request", lambda request: print(f"Request: {request.url}"))

    page.goto('https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php')
    page.fill('input[name="username"]', 'your_username')  # 실제 아이디로 변경
    page.fill('input[name="password"]', 'your_password')  # 실제 비밀번호로 변경
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')  # 페이지 로드 완료 대기
    content = page.content()
    browser.close()
    return content

try:
    with sync_playwright() as playwright:
        html_content = run(playwright)
        st.components.v1.html(html_content, width=1400, height=800)
except Exception as e:
    st.error(f"An error occurred: {e}")
