import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path ='1103/NanumGothic.ttf'
font_prop = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_prop)

image_names= ['image1','image2','image3']
accuracies = [92.5, 85.3, 89.1]

plt.bar(image_names, accuracies)
plt.title("OCR 인식률 비교")
plt.xlabel("이미지 이름")
plt.ylabel("인식률 (%)")
plt.ylim(0,100)
plt.show()