import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    st.title('Selenium with Streamlit')
    st.write('Click the button to open Google.')

    if st.button('Open Google'):
        # Set up Selenium and Chrome WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Initialize WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        url = 'https://www.google.com'
        driver.get(url)
        st.write('Google opened in Selenium WebDriver.')

        # Capture a screenshot
        screenshot = driver.get_screenshot_as_png()
        st.image(screenshot)

        # Clean up
        driver.quit()

if __name__ == '__main__':
    main()
