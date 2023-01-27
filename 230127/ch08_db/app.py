from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew') # 데이터 입력 Form
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST', 'GET']) # student.html에서 입력한 값들을 post로 전달
def addrec():
    if request.method == 'POST':
        # 데이터를 입력받아서 INSERT
        try:
            # HTML 프론트에서 데이터를 입력받음
            nm = request.form['nm']
            add = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            # DB에 해당 값들을 각각 입력
            #                 # DB 서버 주소 입력
            with sql.connect('database.db') as con:
                # DB 입력창에 입력커서 활성화
                cur = con.cursor()

                # DB에 값 입력 (일시적인 메모리 사용)
                cur.execute('INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)',(nm,add,city,pin))

                # DB에 값 저장. (DB에 입력 완료)
                con.commit()

                msg = "DB 저장 완료"
        except:
            con.rollback()
            msg = "DB 입력 에러 발생"
        finally: # except을 걸려도, 무조건 finally는 한번 실행
            # msg = 'Done'
            return render_template('result2.html', msg=msg)
            con.close() # db 닫음
    else:
        pass

@app.route('/list')
def list():
    con = sql.connect('database.db') # DB 파일에 접근
    con.row_factory = sql.Row 
    cur = con.cursor()
    cur.execute("SELECT * FROM students") # 데이터 전체 조회

    rows = cur.fetchall(); # 레코드 단위로 데이터 전달 받음
    return render_template('list.html', rows = rows)

if __name__ == '__main__':
    app.run(debug=True)