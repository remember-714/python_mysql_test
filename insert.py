import pymysql                              #导入pymysql
 
db=pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   db="test",
                   port=3306
                   )                        #创建数据库对象
 
cur = db.cursor()
 
sql = "INSERT INTO `test` (`id`, `name`, `password`) VALUES ('3', 'test1', 'test1')"
 
try:
  cur.execute(sql)                     #执行sql
  db.commit()                          #提交
 
except Exception as e:
  db.rollback()                       #异常回滚
 
finally:
  db.close() 
