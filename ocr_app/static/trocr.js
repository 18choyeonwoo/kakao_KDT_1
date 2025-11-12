// trocr.js
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("upload-form");
    const fileInput = document.getElementById("file-input");
    const canvas = document.getElementById("ocrCanvas");
    const ctx = canvas.getContext("2d");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const file = fileInput.files[0];
        if (!file) return alert("이미지를 선택해주세요!");

        const img = new Image();
        img.onload = async () => {
            canvas.width = img.width;
            canvas.height = img.height + 40;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, 0, 0);

            // 서버에 이미지 업로드
            const formData = new FormData();
            formData.append("file", file);

            try {
                const res = await fetch("http://localhost:8000/ocr", {
                    method: "POST",
                    body: formData
                });
                const data = await res.json();

                // bbox 시각화
                const box = data.bbox;
                ctx.strokeStyle = "red";
                ctx.lineWidth = 2;
                ctx.strokeRect(box.x0, box.y0, box.x1 - box.x0, box.y1 - box.y0);

                // TrOCR 결과 텍스트
                ctx.font = "20px 'Gamja Flower', sans-serif";
                ctx.fillStyle = "blue";
                ctx.fillText(data.text, 10, canvas.height - 10);
            } catch (err) {
                console.error("OCR 서버 에러:", err);
            }
        };
        img.src = URL.createObjectURL(file);
    });
});
