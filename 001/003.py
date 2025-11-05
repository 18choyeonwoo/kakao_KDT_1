### HTML 렌더링

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>이건 h1 제목</h1>
    <p>이건 p 본문 </p>
    <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
    '''

# @app.route('/user')
# def users():
#     return f'Hello, everyone!'

# 디폴트 선언시
@app.route('/user/', defaults={'user_name': '이순신', 'user_id': 7})
@app.route('/user/<user_name>/', defaults={'user_id': 5})
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'


if __name__ == '__main__':
    app.run(debug=True)