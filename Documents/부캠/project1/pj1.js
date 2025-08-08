document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const nameInput = document.getElementById("name");
    const dateInput = document.getElementById("date");
    const timeInput = document.getElementById("time");
    const phoneInput = document.getElementById("phone");
    const foodInputs = document.getElementsByName("food");
    const moneyCheckbox = document.getElementById("money");

    const decreaseBtn = document.getElementById('decrease');
    const increaseBtn = document.getElementById('increase');
    const countSpan = document.getElementById('count');

    let count = 1;

    increaseBtn.addEventListener('click', () => {
        if (count < 6) {
            count++;
            countSpan.textContent = count;
        }
    });

    decreaseBtn.addEventListener('click', () => {
        if (count > 1) {
            count--;
            countSpan.textContent = count;
        }
    });

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        if (nameInput.value.trim() === "") {
            alert("이름을 입력해주세요.");
            nameInput.focus();
            return;
        }

        if (!moneyCheckbox.checked) {
            alert("예약금을 입금하셔야 예약이 가능합니다.");
            return;
        }

        // 메뉴 선택 검사
        let selectedFood = "";
        for (let i = 0; i < foodInputs.length; i++) {
            if (foodInputs[i].checked) {
                selectedFood = foodInputs[i].value;
                break;
            }
        }

        if (selectedFood === "") {
            alert("메뉴를 선택해주세요.");
            return;
        }

        alert(`예약이 완료되었습니다! 🎉\n이름: ${nameInput.value}\n인원 수: ${count}\n선택 메뉴: ${selectedFood}`);
        form.reset();
        count = 1;
        countSpan.textContent = count;
    });

    // 오늘 이전 날짜 선택 못하게
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
});
