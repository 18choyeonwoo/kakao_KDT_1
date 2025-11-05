from flask import Flask, jsonify, make_response, request, render_template, redirect, url_for
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL 데이터베이스 연결
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',  # root 비밀번호 입력
        database='mydb'
    )
    return conn

# 모든 고객 정보 가져오기
def get_all_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM customer')
    customers = cursor.fetchall()
    conn.close()
    return customers

# 고객 추가
def add_customer(customer_id, name, age, gender, purchase_amount, purchase_date):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customer (id, name, age, gender, purchase_amount, purchase_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (customer_id, name, age, gender, purchase_amount, purchase_date))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.IntegrityError:
        # Primary Key 중복 등 예외 처리
        return False

# 고객 정보 수정
def update_customer(customer_id, name, age, gender, purchase_amount, purchase_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE customer
        SET name=%s, age=%s, gender=%s, purchase_amount=%s, purchase_date=%s
        WHERE id=%s
    ''', (name, age, gender, purchase_amount, purchase_date, customer_id))
    conn.commit()
    conn.close()

# 고객 삭제
def delete_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customer WHERE id=%s', (customer_id,))
    conn.commit()
    conn.close()

# 루트
@app.route('/', methods=['GET'])
def index():
    customers = get_all_customers()
    columns = ["고객ID", "이름", "나이", "성별", "구매금액", "구매날짜"]
    return render_template('index2.html', customers=customers, columns=columns)

# 고객 추가
@app.route('/add', methods=['POST'])
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

# 고객 수정
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

# 고객 삭제
@app.route('/delete/<customer_id>', methods=['POST'])
def delete(customer_id):
    delete_customer(customer_id)
    return redirect(url_for('index'))

# 웹 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
