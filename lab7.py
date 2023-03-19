import mysql.connector
conn = mysql.connector.connect(host='localhost',
                                       database='dbmslab',
                                       user='root',
                                       password='Geeky@Zain98')
cursor=conn.cursor(buffered=True)
cursor.execute('SHOW tables')
for x in cursor:
    print(x)
    

cursor.execute("DESCRIBE teaches")
records=cursor.fetchall()
for x in records:
    print(x)

#cursor.execute("create view faculty1 as select ID ,name,dept_name from instructor")

