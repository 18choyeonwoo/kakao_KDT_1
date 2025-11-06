from flask import Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
from .ocr import extract_text, extract_text_ez
from . import db
import os

main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class OCRResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120))
    tesseract_text = db.Column(db.Text)
    easyocr_text = db.Column(db.Text)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return jsonify({'error': '올바른 이미지 파일이 아닙니다.'}), 400
    # 파일 저장
    filename = secure_filename(file.filename)
    filepath = os.path.join(os.getcwd(), 'ocr_app/static/uploads', filename)
    file.save(filepath)
    # ocr 실행
    tesseract_text = extract_text(filepath)
    easyocr_text = extract_text_ez(filepath)

    result = OCRResult(
        filename=filename,
        tesseract_text=tesseract_text,
        easyocr_text=easyocr_text
    )
    db.session.add(result)
    db.session.commit()

    # ✅ 두 OCR 결과 모두 반환
    return jsonify({
        'filename': filename,
        'tesseract_result': tesseract_text,
        'easyocr_result': easyocr_text
    })
