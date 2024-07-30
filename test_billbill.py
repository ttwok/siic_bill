import streamlit as st

st.title("Streamlit Web Automation Example")

# 리디렉션할 URL 설정
url = "https://www.naver.com"

# JavaScript 코드 작성: 페이지 열고, 검색어 입력하고, 검색 버튼 클릭
js_code = """
    var url = 'https://www.naver.com';
    var newWindow = window.open(url, '_blank');
    newWindow.onload = function() {
        setTimeout(function() {
            var searchInput = newWindow.document.getElementById('query');
            searchInput.value = '카페24';
            var searchButton = newWindow.document.querySelector('button.spm');
            searchButton.click();
        }, 1000); // 1초 지연 후 실행
    };
"""

# 버튼 클릭 시 JavaScript 실행
if st.button("Connect to Naver and Search 카페24"):
    st.components.v1.html(f'<script>{js_code}</script>')

# 대체 링크 제공
st.markdown(f'<a href="{url}" target="_blank">Open Naver in a new tab</a>', unsafe_allow_html=True)
