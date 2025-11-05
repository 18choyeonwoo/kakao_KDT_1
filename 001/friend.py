from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('friend.html')

@app.route('/friend', methods=['GET', 'POST'])
def friend():
    if request.method == 'POST':
        data = {
            "이름": request.form.get('name'),
            "생년월일": request.form.get('birth'),
            "전화번호": request.form.get('phone'),
            "이메일": request.form.get('email'),
            "MBTI": request.form.get('mbti')
        }
        return jsonify(data)
    else:  # GET 방식
        name = request.args.get('name')
        birth = request.args.get('birth')
        phone = request.args.get('phone')
        email = request.args.get('email')
        mbti = request.args.get('mbti')
        data = {"이름": name, "생년월일": birth, "전화번호": phone, "이메일": email, "MBTI": mbti}
        return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

