from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# ===============================
# 공통 설정
# ===============================
BASE_UPLOAD_DIR = 'static/uploads'
app.config['UPLOAD_FOLDER'] = BASE_UPLOAD_DIR
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ===============================
# 1️⃣ 친구 연락사항 JSON 리턴
# ===============================
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    # POST로 데이터 받기
    name = request.form.get('name')
    birth = request.form.get('birth')
    phone = request.form.get('phone')
    email = request.form.get('email')
    mbti = request.form.get('mbti')

    data = {
        "이름": name,
        "생년월일": birth,
        "전화번호": phone,
        "이메일": email,
        "MBTI": mbti
    }

    return jsonify(data)


# ===============================
# 2️⃣ 이미지 업로드 (카테고리별 저장)
# ===============================
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    category = request.form.get('category')
    if not category:
        return '카테고리 이름을 입력하세요.'

    if 'file' not in request.files:
        return '파일이 업로드되지 않았습니다.'
    file = request.files['file']

    if file.filename == '':
        return '파일이 선택되지 않았습니다.'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
        os.makedirs(category_path, exist_ok=True)
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


# ===============================
# 3️⃣ 갤러리: 업로드된 이미지 보기
# ===============================
@app.route('/gallery')
def gallery():
    categories = []
    if os.path.exists(BASE_UPLOAD_DIR):
        categories = os.listdir(BASE_UPLOAD_DIR)
    images = {}
    for cat in categories:
        path = os.path.join(BASE_UPLOAD_DIR, cat)
        if os.path.isdir(path):
            images[cat] = os.listdir(path)
    return render_template('gallery.html', images=images)


# ===============================
# 실행
# ===============================
if __name__ == '__main__':
    os.makedirs(BASE_UPLOAD_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

