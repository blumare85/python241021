#db1.py
import sqlite3

#일단 메모리에서 연습
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(r'c:\work\sample.db')

#커서 인스턴스 생성
cursor = conn.cursor()

#테이블 구조 생성
cursor.execute("create table if not exists PhoneBook(Name text, PhoneNum text);")

#1건 데이터 입력
cursor.execute("insert into PhoneBook values('derick', '010-222-3333');")

#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-111-2222"
cursor.execute("insert into PhoneBook values(?, ?);", (name, phoneNumber))

#여러건 데이터 입력
datalist = (("전우치", "010-333-4444"), ("박문수", "010-555-6666"))
cursor.executemany("insert into PhoneBook values(?, ?);", datalist)

#입력 데이터 확인
cursor.execute("select * from PhoneBook")
#for row in cursor:
#    print(row[0], row[1])
print(cursor.fetchall())
#print(cursor.fetchmany(2))
#print(cursor.fetchone())

#완료
conn.commit()