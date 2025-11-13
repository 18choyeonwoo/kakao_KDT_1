from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
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
def root():
    if 'username' in session:
        return redirect(url_for('main.home'))
    return redirect(url_for('auth.login'))


# ✅ 로그인한 사람만 접근 가능한 홈 (서비스 선택 페이지)
@main.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    return render_template('home.html', username=session['username'])


# ✅ OCR 서비스 페이지
@main.route('/home/ocr')
def ocr_page():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    return render_template('service/ocr.html', username=session['username'])

# ✅ 배경제거 서비스 페이지
@main.route('/home/img')
def img_page():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    return render_template('service/img.html', username=session['username'])


# ✅ 파일 업로드 및 OCR 처리
@main.route('/upload', methods=['POST'])
def upload():
    if 'username' not in session:
        return jsonify({'error': '로그인이 필요합니다.'}), 403
    
    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return jsonify({'error': '올바른 이미지 파일이 아닙니다.'}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(os.getcwd(), 'ocr_app/static/uploads', filename)
    file.save(filepath)

    tesseract_text = extract_text(filepath)
    easyocr_text = extract_text_ez(filepath)

    result = OCRResult(filename=filename, tesseract_text=tesseract_text, easyocr_text=easyocr_text)
    db.session.add(result)
    db.session.commit()

    return jsonify({
        'filename': filename,
        'tesseract_result': tesseract_text,
        'easyocr_result': easyocr_text
    })
