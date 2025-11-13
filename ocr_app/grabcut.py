import cv2  # OpenCV 라이브러리 임포트
import numpy as np  # NumPy 라이브러리 임포트

folder = "1113/grabcut/"

def remove_background_grabcut(image_path, output_path):
   # 이미지 파일을 읽어옴
   img = cv2.imread(image_path)
   if img is None:
       print(f"Error: Could not read image from {image_path}")  # 이미지가 없을 때 오류 출력
       return

   # GrabCut 처리용 마스크(0 초기화)
   mask = np.zeros(img.shape[:2], np.uint8)

   # 전경(객체)이 포함될 것으로 예상되는 사각형 영역 지정
   # (x, y, width, height) (209, 239, 383, 546)
   # rect = (50, 50, img.shape[1] - 100, img.shape[0] - 100)
   rect = (209, 239, 383 - 209, 546 - 239)

   # GrabCut 알고리즘 적용 위한 임시 배경/전경 모델 배열 생성
   bgdModel = np.zeros((1, 65), np.float64)
   fgdModel = np.zeros((1, 65), np.float64)

   # GrabCut 알고리즘 실행 (rect 방식)
   cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

   # 결과 마스크를 0(배경), 1(전경)로 이진화 
   mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

   # 원본 이미지에 알파 채널(RGBA) 추가 
   result_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

   # 알파 채널에 마스크 적용 (배경: 0, 전경: 255)
   result_rgba[:, :, 3] = mask2 * 255

   # RGBA 이미지 저장
   cv2.imwrite(output_path, result_rgba)
   print(f"Background removed image saved to {output_path}")  # 저장 완료 알림

def apply_post_processing(image_path, output_path_smoothed, output_path_adjusted, blur_kernel_size=(5, 5), transparency_factor=0.7):
   # GrabCut 후처리용 - 이미지 읽어서 RGBA로 사용
   img_rgba = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # 알파 채널 포함해서 이미지 읽기

   # 1. 알파 채널(투명도)만 추출
   alpha_channel = img_rgba[:, :, 3]

   # 2. 알파 채널을 가우시안 블러로 부드럽게 처리 (모서리 부드럽게)
   blurred_alpha = cv2.GaussianBlur(alpha_channel, blur_kernel_size, 0)

   # 3. 블러링된 알파 채널을 다시 이미지에 적용
   smoothed_img_rgba = img_rgba.copy()
   smoothed_img_rgba[:, :, 3] = blurred_alpha
   cv2.imwrite(output_path_smoothed, smoothed_img_rgba)  # 부드럽게 처리된 이미지 저장

   # 4. 전체 이미지의 투명도 조절 (알파 채널에 factor 값 곱하기)
   adjusted_img_rgba = img_rgba.copy()
   adjusted_img_rgba[:, :, 3] = (adjusted_img_rgba[:, :, 3] * transparency_factor).astype(np.uint8)
   cv2.imwrite(output_path_adjusted, adjusted_img_rgba)  # 조절된 투명도 이미지 저장

# 예시 실행 코드
if __name__ == "__main__":
   input_image = f"{folder}example.jpg"  # 입력 이미지 경로
   output_rgba = f"{folder}output_rgba.png"  # GrabCut 결과 저장 경로
   output_smoothed = f"{folder}output_smoothed.png"  # 부드럽게 처리된 이미지 저장 경로
   output_adjusted = f"{folder}output_transparency.png"  # 투명도 조절 이미지 저장 경로

   # GrabCut 배경 제거 함수 실행
   remove_background_grabcut(input_image, output_rgba)

   # 후처리 함수 실행
   apply_post_processing(output_rgba, output_smoothed, output_adjusted, blur_kernel_size=(5, 5), transparency_factor=0.7)