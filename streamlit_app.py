import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    st.title("Streamlit과 Selenium을 이용한 웹 자동화")
    
    url = st.text_input("URL을 입력하세요", "https://www.example.com")
    if st.button("실행"):
        if not url.startswith("http://") and not url.startswith("https://"):
            st.error("올바른 URL 형식이 아닙니다. 'http://' 또는 'https://'로 시작해야 합니다.")
        else:
            run_selenium(url)

def run_selenium(url):
    # Selenium WebDriver 설정 (ChromeDriver 예시)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 브라우저를 숨김 모드로 실행
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(url)
        st.write(f"{url}에 접속했습니다.")
        
        # 새로운 창을 열기
        driver.execute_script("window.open('');")
        # 모든 창 핸들을 가져오기
        handles = driver.window_handles
        # 첫 번째 창에서 두 번째 창으로 전환
        driver.switch_to.window(handles[1])
        st.write("새 창을 열고 전환했습니다.")
        
        # 새 창에서 작업 수행 (예: Google 페이지 열기)
        new_url = "https://www.google.com"
        driver.get(new_url)
        st.write(f"새 창에서 {new_url} 페이지를 열었습니다.")
        
        # 페이지에서 특정 요소를 찾고 상호작용하는 예제
        try:
            element = driver.find_element(By.NAME, "q")
            element.send_keys("Streamlit")
            element.send_keys(Keys.RETURN)
            st.write("검색을 수행했습니다.")
        except Exception as e:
            st.write(f"에러 발생: {e}")
        
        # 작업 완료 후 새 창 닫기
        driver.close()
        # 다시 첫 번째 창으로 전환
        driver.switch_to.window(handles[0])
        st.write("첫 번째 창으로 돌아왔습니다.")
        
    except Exception as e:
        st.error(f"오류 발생: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
