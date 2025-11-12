const loginBtn = document.getElementById('loginBtn');
const loginBox = document.querySelector('.login-box');

loginBtn.addEventListener('click', () => {
    // 로그인창 토글
    loginBox.classList.toggle('active');

    // 버튼 텍스트 토글
    if (loginBox.classList.contains('active')) {
        loginBtn.innerHTML = '&gt;';   // 로그인창 보일 때 >
    } else {
        loginBtn.innerHTML = '&gt; Click to login';  // 로그인창 숨길 때 원래 문구
    }
});
