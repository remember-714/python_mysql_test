import pymysql                              #����pymysql
 
db=pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   db="test",
                   port=3306
                   )                        #�������ݿ����
 
cur = db.cursor()
 
sql = "INSERT INTO `test` (`id`, `name`, `password`) VALUES ('3', 'test1', 'test1')"
 
try:
  cur.execute(sql)                     #ִ��sql
  db.commit()                          #�ύ
 
except Exception as e:
  db.rollback()                       #�쳣�ع�
 
finally:
  db.close() 
