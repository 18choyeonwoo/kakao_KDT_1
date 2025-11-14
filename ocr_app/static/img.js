const form = document.getElementById('upload-form');
const preview = document.getElementById('preview');
const progress = document.getElementById('progress');
const loadingText = document.getElementById('loadingText');
const bar = document.getElementById('bar');

let previewImg = null;
let uploadedFilename = null;

// 1️⃣ 이미지 업로드 → /sam/upload
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('file-input');
    if (!fileInput.files[0]) return alert("이미지를 선택해주세요.");

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    // 썸네일 표시
    const reader = new FileReader();
    reader.onload = e => {
        preview.innerHTML = `<img id="preview-img" src="${e.target.result}" width="300" style="cursor:pointer;">`;
        previewImg = document.getElementById("preview-img");
        previewImg.addEventListener('click', handleImageClick);
    };
    reader.readAsDataURL(fileInput.files[0]);

    try {
        const res = await fetch('/sam/upload', { method: 'POST', body: formData });
        const data = await res.json();
        if (!data.success) throw new Error("업로드 실패");

        uploadedFilename = data.filename;
    } catch (err) {
        alert("업로드 오류: " + err.message);
    }
});


// 2️⃣ 사용자가 클릭 → /sam/segment 호출
async function handleImageClick(event) {
    if (!previewImg) return;

    const rect = previewImg.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    const points = [[Math.floor(x), Math.floor(y)]];
    const labels = [1]; // 클릭한 객체 분리

    // 진행바 표시
    progress.style.display = 'block';
    let percent = 0;
    bar.style.width = '0%';
    loadingText.textContent = '분할 중... 0%';
    const fakeProgress = setInterval(() => {
        percent += Math.random() * 10;
        if (percent >= 90) percent = 90;
        bar.style.width = percent + '%';
        loadingText.textContent = `분할 중... ${Math.floor(percent)}%`;
    }, 300);

    try {
        const res = await fetch('/sam/segment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ points, labels })
        });
        if (!res.ok) throw new Error("서버 분할 오류");

        const blob = await res.blob();
        const url = URL.createObjectURL(blob);

        clearInterval(fakeProgress);
        bar.style.width = '100%';
        loadingText.textContent = '완료! 100%';

        previewImg.src = url;
        progress.style.display = 'none';
    } catch (err) {
        clearInterval(fakeProgress);
        progress.style.display = 'none';
        alert("오류: " + err.message);
    }
}



// 3️⃣ 저장 버튼 → /sam/save_final 호출
saveBtn.addEventListener('click', async () => {
    if (!uploadedFilename) return alert("저장할 이미지가 없습니다.");

    try {
        const res = await fetch('/sam/save_final', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ filename: uploadedFilename })
        });
        const data = await res.json();
        if (!data.success) throw new Error("저장 실패");

        alert("저장 완료! URL: " + data.saved_url);
    } catch (err) {
        alert("저장 오류: " + err.message);
    }
});