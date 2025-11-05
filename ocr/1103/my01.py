from PIL import Image, ImageFilter, ImageOps
import pytesseract

img = Image.open('01.jpg')

#1. 흑백 변환
img = img.convert('L')

#2. 대비(contrast) 강화
img = ImageOps.autocontrast(img)

#3. 노이즈 제거 및 선명화
img = img.filter(ImageFilter.MedianFilter(size=3))

#4. OCR
text = pytesseract.image_to_string(img, lang='kor')
print(text)
