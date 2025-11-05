import pytesseract
import easyocr
import numpy as np
import editdistance

# CER : 문자 단위의 오류율, 0이면 일치
def cer(reference, hypothesis):
   ref = list(reference)
   hyp = list(hypothesis)
   distance = editdistance.eval(ref, hyp)
   cer_value = distance / max(len(ref), 1)
   return cer_value

# WER : 단어 단위
def wer(reference, hypothesis):
   ref = reference.split()
   hyp = hypothesis.split()
   distance = editdistance.eval(ref, hyp)
   wer_value = distance / max(len(ref), 1)
   return wer_value

# 이미지 경로 또는 이미지 배열
image_path = '1105/01.jpg'

# Tesseract OCR 인식
tesseract_text = pytesseract.image_to_string(image_path, lang='kor')

# EasyOCR 인식 (한국어 포함)
reader = easyocr.Reader(['ko', 'en'])
easyocr_result = reader.readtext(image_path, detail=0, paragraph=True)
easyocr_text = ' '.join(easyocr_result)

# 기준 정답 텍스트
with open('1105/real.txt', 'r', encoding='utf-8') as f:
    ground_truth = f.read().strip()

# CER, WER 계산
print("Tesseract CER:", cer(ground_truth, tesseract_text))
print("Tesseract WER:", wer(ground_truth, tesseract_text))
print("EasyOCR CER:", cer(ground_truth, easyocr_text))
print("EasyOCR WER:", wer(ground_truth, easyocr_text))
