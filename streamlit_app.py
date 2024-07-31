import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    st.title("Streamlit과 Selenium을 이용한 웹 자동화")
    
    url = st.text_input("URL을 입력하세요", "http://example.com")
    if st.button("실행"):
        run_selenium(url)

def run_selenium(url):
    # Selenium WebDriver 설정 (ChromeDriver 예시)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 브라우저를 숨김 모드로 실행
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    st.write(f"{url}에 접속했습니다.")
    
    # 페이지에서 특정 요소를 찾고 상호작용하는 예제
    try:
        element = driver.find_element_by_name("q")
        element.send_keys("Streamlit")
        element.send_keys(Keys.RETURN)
        st.write("검색을 수행했습니다.")
    except Exception as e:
        st.write(f"에러 발생: {e}")
    
    driver.quit()

if __name__ == "__main__":
    main()
