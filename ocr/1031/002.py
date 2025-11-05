from flask import Flask, jsonify, make_response, request, render_template, redirect, url_for
from flask_cors import CORS
import json
import sqlite3


app = Flask(__name__)
CORS(app)

# customer.db에 연결하는 함수
# 매번 DB를 열고 닫을 때 반복되는 코드를 간단히 쓰기 위해 정의
def get_db_connection():
    conn = sqlite3.connect('customer.db')
    return conn

conn = get_db_connection()
cursor = conn.cursor()
# SQL 문이 db로 전달되고 커서에 저장됨
cursor.execute('SELECT * FROM customer')
# SELECT 결과의 모든 행을 리스트 형태로 반환
customer_tuples = cursor.fetchall()
#컬럼 이름(id, name..) 만 추출
columns = [desc[0] for desc in cursor.description]
conn.close()

# print(columns)
# print(customer_tuples)


# get_all_customers(): 모든 고객 정보를 가져올 수 있게 함
def get_all_customers():
    # 보편적 쓰이는 세 줄
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customer')
    # -
    customers = cursor.fetchall()
    conn.close()
    return customers

def add_customer(customer_id, name, age, gender, purchase_amount, purchase_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO customer (id, name, age, gender, purchase_amount, purchase_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (customer_id, name, age, gender, purchase_amount, purchase_date))
    conn.commit()
    conn.close()
    return True

def update_customer(customer_id, name, age, gender, purchase_amount, purchase_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE customer
        SET name=?, age=?, gender=?, purchase_amount=?, purchase_date=?
        WHERE id=?
    ''', (name, age, gender, purchase_amount, purchase_date, customer_id))
    conn.commit()
    conn.close()

def delete_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customer WHERE id=?', (customer_id,))
    conn.commit()
    conn.close()

# 루트로 들어오면
@app.route('/', methods=['GET'])
#index 함수 실행
def index():
    customers = get_all_customers()
    columns = ["고객ID", "이름", "나이", "성별", "구매금액", "구매날짜"]
    # 템플릿 엔진이 데이터를 html로 전달해준다. 
    return render_template('index.html', customers=customers, columns=columns)


# 고객 추가 버튼 눌렀을 때
@app.route('/add', methods= ['POST'])
def add():
    customer_id = request.form['customer_id']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    purchase_amount = request.form['purchase_amount']
    purchase_date = request.form['purchase_date']

    if not add_customer(customer_id, name, age, gender, purchase_amount, purchase_date):
        return render_template('error.html', message="ID가 이미 존재합니다.")
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    customer_id = request.form['customer_id']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    purchase_amount = request.form['purchase_amount']
    purchase_date = request.form['purchase_date']
    update_customer(customer_id, name, age, gender, purchase_amount, purchase_date)
    return redirect(url_for('index'))

@app.route('/delete/<customer_id>', methods=['POST'])
def delete(customer_id):
    delete_customer(customer_id)
    return redirect(url_for('index'))

# 웹서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

