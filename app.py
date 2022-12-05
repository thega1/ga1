from flask import Flask,render_template,request
import pymysql
app = Flask(__name__)
def sqlcon():
    con=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123123',
        database='user'
    )
    return con

@app.route('/')
def login():  # put application's code here
    return render_template('pages-login.html')
@app.route('/logins',methods=['POST','GET'])
def ss():
    password=(request.values.get('password'))
    username=request.values.get('username')

    #在数据库中查询
    con=sqlcon()
    cursor=con.cursor()
    sql="select * from user where username='{}' and password = '{}'".format(username,password)
    print("select * from user where username='{}' and password = '{}'".format(username,password))
    cursor.execute(sql)
    res = cursor.fetchone()
    if res is None:
        return 'no'
    else:
        return 'yes'

@app.route('/pages-register.html')
def reg():
    return render_template('pages-register.html')

if __name__ == '__main__':
    app.run()