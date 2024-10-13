#!/opt/flask/bin/python
from flask import Flask, render_template, request, redirect, url_for
from ldap3 import Server, Connection, ALL

import requests, psutil

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

@app.route('/score')
def score_page():
    
    
   dict = {'phy':50,'che':60,'maths':70}
   server_details = {'method':request.method,
                     'remote_addr':request.remote_addr,
                     'user_agent':request.user_agent.string,
                     'cpu_load': psutil.cpu_percent(interval=1),
                     'memory_info': psutil.virtual_memory() 
                     }    
   return render_template('admin_pages/1_score.html',result=dict, username=username, server=server_details)
 
@app.route('/tester')
def website_tester():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)