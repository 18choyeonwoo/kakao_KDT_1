from PIL import Image
import pytesseract

img = Image.open('1105/01.jpg')
# 전처리: 이미지 품질 개선
text = pytesseract.image_to_string(img, lang='kor')
# 후처리: 정규표현식 등 써서 불필요한 문자 제거
print(text)
