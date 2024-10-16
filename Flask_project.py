#!/opt/flask/bin/python
from flask import Flask, render_template, request, redirect, url_for, jsonify
from ldap3 import Server, Connection, ALL
from System_Monitor import SystemMonitorClass
from Http_Requests import HttpRequestsClass
import psutil, datetime

username = None


app = Flask(__name__)
system_monitor = SystemMonitorClass()
http_data = HttpRequestsClass()


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

@app.route('/system_monitoring')
def system_monitoring_page(): 
   dict = {'phy':50,'che':60,'maths':70}
   server_details = { 'cpu_load' : system_monitor.get_memory_info(),
                      'memory_info' : system_monitor.get_cpu_load(),
                      'boot_time' : system_monitor.get_boot_time(),
                      'disk_io' : system_monitor.get_disk_io_counters()
                     }    
   return render_template('admin_pages/1_SystemMonitoring.html',result=dict, username=username, server=server_details)
 
@app.route('/http_data')
def http_data_page(): 
   url = "https://www.google.com" 
   http_details = { 'status_code': http_data.get_status_code(url),
                    'total_seconds' : http_data.get_response_time(url)
                    }  
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('admin_pages/2_http.html',result=dict, username=username, http=http_details)




@app.route('/url_form')
def input_form():
    return render_template('admin_pages/url_input_form.html')

@app.route('/result', methods=['POST'])
def result_page():
    # Get the data from the form
    data = request.form.get('data')  # Using .get() for safe access
    return render_template('admin_pages/url_result.html', data=data)

 
  


 

@app.route('/tester')
def website_tester():
    pass

@app.route('/user_info')
def user_info():
    return render_template('admin_pages/4_User_Info_Dashboard.html')

@app.route('/api/userinfo', methods=['GET'])
def api_user_info():
    if username:
        return jsonify({'username':username, 'message': f'Hello, {username}!'})
    else:
        return jsonify({'error': 'User not logged in.'}) 
    
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)