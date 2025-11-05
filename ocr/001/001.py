### Route 구성

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!!!'


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
    
# [host]
# host='127.0.0.1' (기본값) - localhost
# host='0.0.0.0' - 모든 대역대 ip에서 접근
# host='10.0.66.200' - 특정 ip에서만 접근

# [debug]
# True: 오류정보 표시, 소스수정시 재시작
# False: (기본값)

# [reload]
# True: 소스수정시 재시작
# False: (기본값)

# [port]
# 5000 (기본값)
