import Levenshtein


def calculate_accuracy(original_text, ocr_text):
   distance = Levenshtein.distance(original_text, ocr_text)
   max_len = max(len(original_text), len(ocr_text))
   accuracy = (1 - distance / max_len) * 100
   return accuracy


# 예: 원문과 OCR 결과 텍스트
with open('real.txt', 'r', encoding='utf-8') as f:
    original = f.read().strip()
with open('01.txt', 'r', encoding='utf-8') as f:
    ocr_result_01 = f.read().strip()
with open('02.txt', 'r', encoding='utf-8') as f:
    ocr_result_02 = f.read().strip()
with open('03.txt', 'r', encoding='utf-8') as f:
    ocr_result_03 = f.read().strip()

accuracy_01 = calculate_accuracy(original, ocr_result_01)
accuracy_02 = calculate_accuracy(original, ocr_result_02)
accuracy_03 = calculate_accuracy(original, ocr_result_03)
print(f"01. OCR 인식률: {accuracy_01:.2f}%")
print(f"02. OCR 인식률: {accuracy_02:.2f}%")
print(f"03. OCR 인식률: {accuracy_03:.2f}%")
