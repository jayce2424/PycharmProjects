import mysql.connector

con = mysql.connector.connect(
    host="192.168.10.200", port="3306",
    user="app", password="app123",
    database="jqx"
)
cursor=con.cursor()
sql="select empno,ename,hiredate from t_emp;"
cursor.execute(sql)
for one in cursor:
    print(one[0],one[1],one[2])
con.close()
