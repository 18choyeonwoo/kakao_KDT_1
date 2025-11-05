from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    #method = request.method
    #return method
    if request.method == 'POST':
        username = request.form.get('username')
        userid = request.form.get('userid')
        # .get(): 딕셔너리 값을 안전하게 가져오는 메소드

        if userid:
            return f'<h1>어서오세요 {username}[{userid}]</h1>'
        else:
            return '<h1>UserID 값이 없습니다.</h1>'

        #return request.form # 딕셔너리 구조
    return render_template("form.html")

@app.route("/etc", methods=['GET','POST'])
def etc():
    return request.args # 딕셔너리 구조
    
if __name__ == '__main__':
    app.run(debug=True)