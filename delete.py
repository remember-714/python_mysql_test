import pymysql                              #导入pymysql
 
db=pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   db="test",
                   port=3306
                   )                        #创建数据库对象
 
cur = db.cursor()     
 
sql = "DELETE from test where id = %d"
 
try:
  cur.execute(sql% (2))
  db.commit()
 
except Exception as e:
  db.rollback()
 
finally:
  db.close()
