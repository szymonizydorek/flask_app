from datetime import datetime

class UserManager():
    
    def __init__(self, login, password, time):
        self.login = login
        self.password = password
        self.login_time = time 
        
    def login(self):
        self.login_time = datetime.now()
        
    def get_info(self):
        return {
        'username' : self.username,
        'password' : self.password
        }