import sqlite3

columns = ["고객ID", "이름", "나이", "성별", "구매금액", "구매날짜"]
customer_tuples = [
    ("C001", "김철수", 35, "남성", 150000, "2024-03-15"),
    ("C002", "이영희", 28, "여성", 280000, "2024-03-14"),
    ("C003", "박민수", 42, "남성", 95000, "2024-03-13")
]

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()

# 테이블 생성 (없으면)
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    purchase_amount INTEGER,
    purchase_date TEXT
)
''')

# 기존 데이터 삭제 (중복 입력 방지용)
## 테이블 구조는 남고, 내용만 없어집니다.
cursor.execute('DELETE FROM customer')

# 데이터 삽입
## customer_tuples의 내용을 차례로 넣습니다.
cursor.executemany('''
INSERT INTO customer (id, name, age, gender, purchase_amount, purchase_date)
VALUES (?, ?, ?, ?, ?, ?)
''', customer_tuples)


#실제로 customer.db 파일에 반영되고, 프로그램 종료됩니다.
conn.commit()
conn.close()

