from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def login():  # put application's code here
    return render_template('pages-login.html')
@app.route('/logins')
def ss():
    return "ac"
@app.route('/pages-register.html')
def reg():
    return render_template('pages-register.html')

if __name__ == '__main__':
    app.run()
