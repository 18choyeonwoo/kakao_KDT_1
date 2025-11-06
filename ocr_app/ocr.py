import pytesseract
from PIL import Image
import easyocr
import numpy as np

# 1. pytesseract
def extract_text(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path), lang='kor+eng')
        return text.strip()
    except Exception as e:
        return f"Tesseract Error: {str(e)}"

# 2. easyocr
def extract_text_ez(image_path, min_confidence=0.5):
    try:
        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(image_path, detail=0)
        return "\n".join(results).strip()
    except Exception as e:
        return f"EasyOCR Error: {str(e)}"