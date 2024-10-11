#!/opt/flask/bin/python
from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def index_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'password':
        return f'Welcome, {username}!'
    else:
        return f'{username} and your password are incorrect', 401
 
    return f'Username: {username}, password:{password}'


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)