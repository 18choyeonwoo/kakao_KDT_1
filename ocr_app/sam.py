from ultralytics.models.sam import Predictor as SAMPredictor
import cv2
import numpy as np
import os



def remove_background_with_sam_and_grabcut(image_path, output_path_grabcut,
                                           output_path_smoothed, output_path_adjusted,
                                           sam_point, sam_label, blur_kernel_size=(5,5),
                                           transparency_factor=0.7):
    # SAM Predictor 초기화 (요청 시점에)
    overrides = dict(conf=0.25, task="segment", mode="predict", imgsz=1024, model="mobile_sam.pt")
    predictor = SAMPredictor(overrides=overrides)
    image_bgr = cv2.imread(image_path)
    if image_bgr is None:
        raise ValueError(f"이미지를 읽을 수 없습니다: {image_path}")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    predictor.set_image(image_rgb)

    input_points = np.array([sam_point])
    labels = np.array([sam_label])
    results = predictor(points=[input_points], labels=[labels])
    sam_mask = results[0].masks.data[0].cpu().numpy().astype(np.uint8)

    # 알파 채널 적용
    result_rgba = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2BGRA)
    result_rgba[:, :, 3] = (1 - sam_mask) * 255  # mask 반전

    # PNG로 저장
    cv2.imwrite(output_path_grabcut, result_rgba)

    # 가우시안 블러
    blurred_alpha = cv2.GaussianBlur(result_rgba[:, :, 3], blur_kernel_size, 0)
    smoothed_img = result_rgba.copy()
    smoothed_img[:, :, 3] = blurred_alpha
    cv2.imwrite(output_path_smoothed, smoothed_img)

    # 투명도 조절
    adjusted_img = result_rgba.copy()
    adjusted_img[:, :, 3] = (adjusted_img[:, :, 3] * transparency_factor).astype(np.uint8)
    cv2.imwrite(output_path_adjusted, adjusted_img)
