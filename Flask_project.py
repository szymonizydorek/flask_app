#!/opt/flask/bin/python
from flask import Flask, render_template, request, redirect, url_for

username = None

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

#The route() decorator in Flask is used to bind URL to a function.
@app.route('/login', methods=['POST'])
def index_login():
    global username  
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'password':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user'))
    
@app.route('/admin')
def hello_admin():
   return render_template('hello_admin.html', username=username)
 
@app.route('/user')
def hello_user():
   return f'Hello user {username}'
 
@app.route('hello/<init:score>')
def hello_name(score):
    return render_template('score.html', marks =)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)