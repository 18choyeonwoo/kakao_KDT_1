from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    #if request.method == 'POST':
    username = request.form.get('username')
    userid = request.form.get('userid')
    if userid:
        return f'<h1>어서오세요 {username}님!</h1>'
    else:
        #return '<h1>userid가 제공되지 않았습니다.</h1>'
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)