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
def GetData():
    con = sqlcon()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM `user`')
    data = cursor.fetchall()
    return data
@app.route('/')
def login():  # put application's code here
    return render_template('pages-login.html')
@app.route('/logins',methods=['POST','GET'])
def ss():
    password=(request.values.get('password'))
    username=request.values.get('username')
    if username=='202122150107':
        return render_template('tables-general.html')

    #在数据库中查询
    con=sqlcon()
    cursor=con.cursor()
    sql="select * from user where username='{}' and password = '{}'".format(username,password)
    cursor.execute(sql)
    res = cursor.fetchone()


    if res is None:
        return "your username or password is wrong"
    else:
        data=GetData()
        return render_template('tables-general.html',datas=data)

@app.route('/pages-register.html',methods=['POST','GET'])
def reg():
    print(request.values)
    con=sqlcon()
    cur=con.cursor()
    if request.values.get('name') is None:
        return render_template('pages-register.html')
    else:
        username = request.values.get('name')
        email = request.values.get('email')
        password = request.values.get('password')
        sql = "insert into user values ('0','{}','{}','{}') ".format(username,email,password)
        print(sql)
        con = sqlcon()
        cur = con.cursor()
        print(sql)
        cur.execute(sql)
        con.commit()
        return "注册成功"

@app.route('/update',methods=['POST','GET'])
def update():
    id=request.values.get('id')
    username=request.values.get('name')
    password=request.values.get('password')
    email=request.values.get('email')
    
    return render_template('forms-layouts.html',id=id,username=username,password=password,email=email)

if __name__ == '__main__':
    app.run()