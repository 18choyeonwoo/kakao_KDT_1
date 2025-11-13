from flask import Blueprint, request, jsonify, current_app
import os
from werkzeug.utils import secure_filename
from .sam import remove_background_with_sam_and_grabcut

sam_bp = Blueprint('sam_bp', __name__, url_prefix='/sam')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@sam_bp.route('/upload', methods=['POST'])
def sam_upload():
    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return jsonify({'error':'올바른 이미지 파일이 아닙니다.'}), 400
    
    filename = secure_filename(file.filename)
    save_folder = os.path.join(current_app.static_folder, 'uploads')
    os.makedirs(save_folder, exist_ok=True)
    filepath = os.path.join(save_folder, filename)
    file.save(filepath)

    # SAM 처리 후 저장 경로도 원본 파일명 그대로
    output_path = filepath  # grabcut_ 없이 덮어쓰기
    output_smooth = os.path.join(save_folder, f"smooth_{filename}")
    output_transparency = os.path.join(save_folder, f"transparency_{filename}")

    # SAM 점 프롬프트와 레이블 (JS에서 나중에 받을 수도 있음)
    sam_point = [300,400]
    sam_label = 1

    try:
        remove_background_with_sam_and_grabcut(
            filepath,
            output_path,
            output_smooth,
            output_transparency,
            sam_point,
            sam_label
        )
    except Exception as e:
        return jsonify({'error': f'SAM 처리 실패: {str(e)}'}), 500
    # 웹에서 접근 가능한 URL 반환
    result_url = f"/static/uploads/{filename}"  # 그대로 사용
    return jsonify({'filename': filename, 'result_url': result_url})
