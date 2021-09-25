import mysql.connector
class Database:
    def __init__(self):
        self.app = None
        self.driver = None
    
    def init_app(self, app):
        self.app = app
        self.connect()
    
    def connect(self):
        self.driver =  mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "mysql"
            )
        print('------------------------------------------')
        print(self.driver)
        print('------------------------------------------')
        return self.driver
    
    def get_db(self):
        if not self.driver:
            print('NOT PRESENT')
            conn = self.connect()
            return conn.cursor()
        print('present')
        return self.driver.cursor()