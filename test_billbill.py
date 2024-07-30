import streamlit as st

st.title("Automated Login to Cafe24")

# 로그인 정보 입력
user_id = st.text_input("Enter your user ID", "dwcha")
password = st.text_input("Enter your password", "cafe24@002", type="password")
login_url = "https://siic-admin-local.cafe24.com/admin/sic/mbr/mbr_wdr_tab.php"

# 자바스크립트 코드 작성: 로그인 페이지 열고, 폼에 입력 값 설정
js_code = f"""
    <script>
        function openAndLogin() {{
            var url = "{login_url}";
            var newWindow = window.open(url, '_blank');
            newWindow.onload = function() {{
                setTimeout(function() {{
                    var userIdInput = newWindow.document.querySelector('input[name="adm_id"]');
                    var passwordInput = newWindow.document.querySelector('input[name="adm_pw"]');
                    if (userIdInput && passwordInput) {{
                        userIdInput.value = "{user_id}";
                        passwordInput.value = "{password}";
                        var loginButton = newWindow.document.querySelector('button.btnLogin span');
                        if (loginButton) {{
                            loginButton.click();
                        }} else {{
                            var form = newWindow.document.querySelector('form');
                            if (form) {{
                                form.submit();
                            }}
                        }}
                    }}
                }}, 1000);
            }};
        }}
        openAndLogin();
    </script>
"""

# 버튼 클릭 시 자바스크립트 실행
if st.button("Login to Cafe24"):
    st.components.v1.html(js_code, height=0)
    st.success("Login process initiated. Please check the new tab.")
