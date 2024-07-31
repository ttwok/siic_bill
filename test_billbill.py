from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://siic-admin-local.cafe24.com/admin/sic/rvn/rvn_bil_tab.php')
    page.fill('input[name="username"]', 'user')
    page.fill('input[name="password"]', 'pass')
    page.click('button[type="submit"]')
    content = page.content()
    browser.close()
    return content

with sync_playwright() as playwright:
    html_content = run(playwright)
    st.components.v1.html(html_content, width=1400, height=800)
