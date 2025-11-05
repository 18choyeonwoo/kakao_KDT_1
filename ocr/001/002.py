### 동적 URL 구성

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

# 동적URL: string, int, float (함수의 인자로 사용)
@app.route('/user/', defaults={'user_name': '이순신', 'user_id': 7})
@app.route('/user/<user_name>/', defaults={'user_id': 5})
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
