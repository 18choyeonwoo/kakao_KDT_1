from PIL import Image
import pytesseract

img = Image.open('01.png')
text = pytesseract.image_to_string(img, lang='kor')

#with open('01.txt', 'w', encoding='utf-8') as f:
    #f.write(text)

print('추출된 텍스트: ', text)

