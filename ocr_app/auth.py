# ocr_app/auth.py
from flask import Blueprint, render_template, redirect, url_for, request, flash, session

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/', methods=['GET', 'POST'])
def login():
    # 이미 로그인 중이라면 바로 홈으로
    if 'username' in session:
        return redirect(url_for('main.home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # 간단한 로그인 검증 예시
        if username == 'admin' and password == '1234':
            session['username'] = username
            flash('로그인 성공!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('아이디 또는 비밀번호가 잘못되었습니다.', 'error')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('username', None)
    flash('로그아웃 되었습니다.', 'info')
    return redirect(url_for('auth.login'))
