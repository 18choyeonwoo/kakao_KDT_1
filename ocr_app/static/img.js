const form = document.getElementById('upload-form');
const preview = document.getElementById('preview');
const progress = document.getElementById('progress');
const loadingText = document.getElementById('loadingText');
const bar = document.getElementById('bar');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('file-input');
    if (!fileInput.files[0]) return alert("이미지를 선택해주세요.");

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    // 썸네일 표시
    const reader = new FileReader();
    reader.onload = e => preview.innerHTML = `<img id="preview-img" src="${e.target.result}" width="200">`;
    reader.readAsDataURL(fileInput.files[0]);

    // 진행바 표시
    progress.style.display = 'block';
    bar.style.width = '0%';
    loadingText.textContent = '배경 제거 중... 0%';
    let percent = 0;
    const fakeProgress = setInterval(() => {
        percent += Math.random() * 10;
        if (percent >= 90) percent = 90;
        bar.style.width = percent + '%';
        loadingText.textContent = `배경 제거 중... ${Math.floor(percent)}%`;
    }, 600);

    try {
        // 서버에 업로드 후 JSON 받기
        const res = await fetch('/sam/upload', { method: 'POST', body: formData });
        if (!res.ok) throw new Error("서버 처리 중 오류 발생");

        const data = await res.json(); // <-- 여기서 JSON으로 받아야 함
        clearInterval(fakeProgress);
        bar.style.width = '100%';
        loadingText.textContent = '완료! 100%';

        // 썸네일 이미지를 변환된 이미지로 교체
        const previewImg = document.getElementById('preview-img');
        if (previewImg) {
            previewImg.src = data.result_url;
            // previewImg.width = 400; // 필요하면 크기 조절
        }
        progress.style.display = 'none';
    } catch (err) {
        clearInterval(fakeProgress);
        alert("오류: " + err.message);
        progress.style.display = 'none';
    }
});
