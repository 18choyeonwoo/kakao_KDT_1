from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/conditional/<int:value>')
def conditional_example(value):
    return render_template('conditional_example.html', template_variable=value)

@app.route('/loop/<int:value>')
def loop_example(value):
    return render_template('loop_example.html', template_variable=value)

@app.route('/loop2/<int:value>')
def loop_example2(value):
    return render_template('loop_example2.html', template_variable=value)

@app.route('/dict')
def dict_example():
    template_dict = {"banana": 1, "apple": 2, "orange": 3}
    return render_template('dict_example.html', template_dict=template_dict)


@app.route('/sorted')
def sorted_dict_example():
    template_dict = {"banana": 1, "apple": 2, "orange": 3}
    return render_template('sorted_dict_example.html', template_dict=template_dict)

@app.route('/sorted_dict')
def sorted_dict_example2():
    template_dict = {"banana": 1,"apple": 3,"orange": 2,"grape": 4}

    sort_by = request.args.get('sort_by', 'key')  # 기본값은 'key'
    reverse = request.args.get('reverse', 'false') == 'true'  # 'true'일 경우 역정렬

    return render_template('sorted_dict_example2.html', template_dict=template_dict, sort_by=sort_by, reverse=reverse)

@app.route('/index2')
def index2():
    return render_template("index2.html")

if __name__ == '__main__':
    app.run(debug=True)