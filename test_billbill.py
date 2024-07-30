import pandas as pd
import streamlit as st

# Streamlit 앱 설정
st.title('정산서 업로드 자동화')

# 파일 업로드 위젯
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])

if uploaded_file is not None:
    # 업로드된 파일을 데이터프레임으로 읽기
    df = pd.read_excel(uploaded_file)
    
    # 데이터프레임 표시
    st.write("업로드된 데이터:")
    st.dataframe(df)
    
    # 로그인 정보 입력 받기
    st.sidebar.header('로그인 정보')
    user_id = st.sidebar.text_input('아이디', 'dwcha')
    password = st.sidebar.text_input('비밀번호', 'cafe24@002', type='password')

    # 로그인 버튼
    if st.sidebar.button('로그인'):
        # 엑셀 데이터와 로그인 정보를 저장하여 별도 스크립트 실행
        df.to_csv('uploaded_data.csv', index=False)
        with open('login_info.txt', 'w') as f:
            f.write(f"{user_id}\n{password}")
        
        st.write("로그인 정보와 엑셀 데이터가 저장되었습니다.")
        st.write("로컬 환경에서 `automation_script.py`를 실행하세요.")
else:
    st.warning("엑셀 파일을 업로드해주세요.")
