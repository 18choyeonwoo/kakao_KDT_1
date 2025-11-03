document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const termsCheckbox = document.getElementById("terms");
    const genderInputs = document.getElementsByName("gender");

    form.addEventListener("submit", function (e) {
        e.preventDefault(); // 폼 기본 제출 막기

        // 이름 검사
        if (nameInput.value.trim() === "") {
            alert("이름을 입력해주세요.");
            nameInput.focus();
            return;
        }

        // 이메일 검사
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailInput.value.trim() === "") {
            alert("이메일을 입력해주세요.");
            emailInput.focus();
            return;
        } else if (!emailPattern.test(emailInput.value)) {
            alert("올바른 이메일 형식이 아닙니다.");
            emailInput.focus();
            return;
        }

        // 비밀번호 검사
        if (passwordInput.value.trim() === "") {
            alert("비밀번호를 입력해주세요.");
            passwordInput.focus();
            return;
        }

        // 성별 검사
        let genderChecked = false;
        for (let g of genderInputs) {
            if (g.checked) {
                genderChecked = true;
                break;
            }
        }
        if (!genderChecked) {
            alert("성별을 선택해주세요.");
            return;
        }

        // 약관 동의 검사
        if (!termsCheckbox.checked) {
            alert("약관에 동의하셔야 가입이 가능합니다.");
            return;
        }

        // 모두 통과 시
        alert("회원가입이 완료되었습니다! 🎉");
        form.reset();
    });
});
