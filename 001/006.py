from flask import Flask, url_for, request
app = Flask(__name__)

#@app.route('/profile')
@app.route('/profile/<username>')
def profile(username):
    return '프로필'

with app.test_request_context():
    # 서버실행없이 결과 테스트 함수
    # print(url_for('profile', page=1))
    # print(url_for('profile', name='홍길동', age=25))
    # print(url_for('profile'))
    print(url_for('profile', username="lee"))
    print(url_for('profile', username='hong', age=25, height=180))
    
    print(url_for('static', filename='style.css'))    # 정적(외부)파일 참조
    print(url_for('static', filename='images/img.png'))
    #print(url_for('static2', filename='style.css'))  # 존재하지 않은 함수 호출 (에러 발생)
