### 파일로 템플릿 렌더링

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sub')
def sub():
    return render_template("sub.html")

# 라우트에 정의된 매개변수: URL경로로 매핑
# 라우트 정의되지 않은 매개변수: 모두 쿼리스트링(?key=value)으로 변환된다
@app.route('/user/<username>', methods=['GET','POST'])
def subname(username):
    method = request.method
    #if request.method == 'GET':
    # request.args.get('userid') : GET방식(안전방식:값이 없으면 None)
    # request.args['userid'] : GET방식 (값이 없으면 Error 발생)
    # request.form['userid'] : POST방식
    # return f'<h1>어서오세요 {username}님!</h1>'
    #return request.args
    
    userid = request.args.get('userid') # 없으면 None
    #userid = request.args['userid']
    
    if userid:
        return f'<h1>어서오세요 {username}[{userid}]님!{method}</h1>'
    else:
        return f'<h1>userid가 없어요</h1>{method}'

if __name__ == '__main__':
    app.run(debug=True)