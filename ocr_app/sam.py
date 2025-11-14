from ultralytics.models.sam import Predictor as SAMPredictor
import cv2
import numpy as np
import os

class SAMService:
    def __init__(self):
        overrides = dict(
            conf=0.25,
            task="segment",
            mode="predict",
            imgsz=1024,
            model="sam_b.pt"
        )
        self.predictor = SAMPredictor(overrides=overrides)
        self.current_image = None
        self.current_mask = None

    # 이미지 로드
    def load_image(self, image_path):
        img_bgr = cv2.imread(image_path)
        if img_bgr is None:
            raise ValueError(f"이미지를 읽을 수 없습니다: {image_path}")

        self.current_image = img_bgr
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        self.predictor.set_image(img_rgb)

    # 클릭 기반 SAM segmentation
    def segment_from_click(self, points, labels):
        points = np.array(points)
        labels = np.array(labels)

        results = self.predictor(points=[points], labels=[labels])
        mask = results[0].masks.data[0].cpu().numpy().astype(np.uint8)

        self.current_mask = mask
        return mask

    # 마스크를 알파 채널로 적용하여 PNG 투명 배경 생성
    def export_png_with_alpha(self, output_path):
        if self.current_image is None or self.current_mask is None:
            raise ValueError("이미지 또는 마스크가 준비되지 않았습니다.")

        rgba = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2BGRA)
        rgba[:, :, 3] = (self.current_mask * 255).astype(np.uint8)

        cv2.imwrite(output_path, rgba)
        return output_path
    
    # 최종 PNG 서버 저장용 함수
    def save_final_png(self, filename):
        output_dir = "ocr_app/static/images"
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, filename)
        self.export_png_with_alpha(output_path)

        return output_path
