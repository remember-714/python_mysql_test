import pymysql                              #导入pymysql
 
db=pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   db="test",
                   port=3306
                   )                        #创建数据库对象
 
cur = db.cursor()                           #获取游标
 
sql = "select * from test"
 
try:
    cur.execute(sql)
    res = cur.fetchall()                    #查询多条数据，使用循环进行输出
    #res = cur.fetchone()                   #查询一条 直接输出
    print("id","name","password")
    #print(res)
    for row in res:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id,name,password)
 
except Exception as e:
    raise e
 
finally:
    db.close()
