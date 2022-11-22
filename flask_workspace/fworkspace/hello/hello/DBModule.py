#DBModule.py
import pymysql 

class Database():
    def __init__(self, host="localhost", user="root", 
             password='1234', db='mydb', port=5306):
        self.db = pymysql.connect( host=host, 
         user=user, 
         password=password,
         db=db,
         port=port)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    #insert, update, delete 시 사용
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        self.db.commit()

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone() 
        return row 
    
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall() 
        return rows  
    
    def close(self):
        self.db.close()
    