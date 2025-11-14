from flask import Blueprint, request, jsonify, current_app
import os
from werkzeug.utils import secure_filename
from .sam import SAMService
from flask import send_file
import io
from PIL import Image
import numpy as np


sam_bp = Blueprint('sam_bp', __name__, url_prefix='/sam')
sam_service = SAMService()  # 한 번만 초기화

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#이미지 업로드 → predictor.set_image() 준비
@sam_bp.route('/upload', methods=['POST'])
def sam_upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': '파일이 없습니다.'}), 400

    filename = secure_filename(file.filename)
    save_folder = os.path.join(current_app.static_folder, 'uploads')
    os.makedirs(save_folder, exist_ok=True)
    filepath = os.path.join(save_folder, filename)
    file.save(filepath)

    # SAM 이미지 준비
    sam_service.load_image(filepath)

    return jsonify({
        'success': True,
        'filename': filename,
        'preview_url': f"/static/uploads/{filename}"
    })

# 사용자가 좌표를 보내면 sam마스크 png 반환
@sam_bp.route('/segment', methods=['POST'])
def sam_segment():
    data = request.json
    points = data.get("points")
    labels = data.get("labels")

    mask = sam_service.segment_from_click(points, labels)

    # mask → PNG
    mask_img = Image.fromarray((mask * 255).astype(np.uint8))
    buf = io.BytesIO()
    mask_img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

# 프론트에서 저장 버튼 누르면 서버에 완성png 저장
@sam_bp.route('/save_final', methods=['POST'])
def sam_save_final():
    filename = request.json.get('filename', 'result.png')
    saved_path = sam_service.save_final_png(filename)

    return jsonify({
        'success': True,
        'saved_url': f"/static/images/{filename}"
    })
