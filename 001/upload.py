from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# 업로드 기본 경로 설정
BASE_DIR = 'static/uploads'
app.config['UPLOAD_FOLDER'] = BASE_DIR

# 허용 확장자
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# 파일 확장자 체크 함수
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # 카테고리 이름 받기
    category = request.form.get('category')
    if not category:
        return '카테고리 이름을 입력하세요.'

    # 파일 받기
    if 'file' not in request.files:
        return '파일이 업로드되지 않았습니다.'
    file = request.files['file']

    if file.filename == '':
        return '파일이 선택되지 않았습니다.'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # 카테고리별 폴더 생성
        category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
        os.makedirs(category_path, exist_ok=True)

        # 저장 경로 생성 및 파일 저장
        save_path = os.path.join(category_path, filename)
        file.save(save_path)

        return f'''
        <h3>업로드 완료!</h3>
        <p>카테고리: <b>{category}</b></p>
        <p>파일명: {filename}</p>
        <img src="/{save_path}" width="300" alt="{filename}">
        '''
    else:
        return '허용되지 않는 파일 형식입니다.'

if __name__ == '__main__':
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    app.run(host='0.0.0.0', port=5001, debug=True)

