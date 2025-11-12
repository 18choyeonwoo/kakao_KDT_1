# server.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import base64
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

app = FastAPI()

# CORS 허용 (웹에서 요청 가능)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# TrOCR 모델 로드
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    img_bytes = await file.read()
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    # TrOCR 추론
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # bbox 좌표가 필요하면 Tesseract나 LayoutLM으로 추출 가능
    # 예제에서는 전체 이미지 bbox만 반환
    bbox = {"x0": 0, "y0": 0, "x1": image.width, "y1": image.height}

    return {"text": text, "bbox": bbox, "width": image.width, "height": image.height}
