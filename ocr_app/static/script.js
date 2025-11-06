const form = document.getElementById('upload-form');
const preview = document.getElementById('preview');
const tesseractDiv = document.getElementById('tesseract-result');
const easyocrDiv = document.getElementById('easyocr-result');
const progress = document.getElementById('progress');
const loadingText = document.getElementById('loadingText');
const bar = document.getElementById('bar');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    // 썸네일 표시
    const reader = new FileReader();
    reader.onload = e => preview.innerHTML = `<img src="${e.target.result}" width="200">`;
    reader.readAsDataURL(fileInput.files[0]);

    // 로딩바 표시 시작
    progress.style.display = 'block';
    bar.style.width = '0%';
    loadingText.textContent = '텍스트 변환 중입니다... 0%';
    let percent = 0;
    const fakeProgress = setInterval(() => {
        percent += Math.random() * 10;
        if (percent >= 90) percent = 90;
        bar.style.width = percent + '%';
        loadingText.textContent = `텍스트 변환 중입니다... ${Math.floor(percent)}%`;
    }, 600)
    
    // flask 서버로 업로드
    const res = await fetch('/upload', { method: 'POST', body: formData });
    const data = await res.json();
    clearInterval(fakeProgress);
    bar.style.width = '100%';
    loadingText.textContent = '완료! 100%';

    console.log(res);
    console.log("서버 응답:", data);

    // 0.8초 정도 후 결과 표시 (조금 자연스럽게)
    setTimeout(() => {
        progress.style.display = 'none';

        if (data.error) {
            tesseractDiv.textContent = data.error;
            easyocrDiv.textContent = '';
        } else {
            tesseractDiv.innerHTML = `
                <pre>${data.tesseract_result}</pre>
            `;
            easyocrDiv.innerHTML = `
                <pre>${data.easyocr_result}</pre>
            `;
        }

        // 결과 영역 표시 (애니메이션 효과)
        result.style.display = 'flex';
        setTimeout(() => result.classList.add('show'), 50);
    }, 800);
});
