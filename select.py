import pymysql                              #����pymysql
 
db=pymysql.connect(host="localhost",
                   user="root",
                   password="root",
                   db="test",
                   port=3306
                   )                        #�������ݿ����
 
cur = db.cursor()                           #��ȡ�α�
 
sql = "select * from test"
 
try:
    cur.execute(sql)
    res = cur.fetchall()                    #��ѯ�������ݣ�ʹ��ѭ���������
    #res = cur.fetchone()                   #��ѯһ�� ֱ�����
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
