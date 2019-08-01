import mysql.connector
try:
    con=mysql.connector.connect(
        host="192.168.10.200",
        port=3306,
        user="app",
        password="app123",
        database="jqx"
    )
    con.start_transaction()
    cursor=con.cursor()
    sql="insert into t_emp(empno,ename,job,mgr,hiredate,sal,comm,deptno)" \
        "values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(9600,"赵娜","SALEMAN",None,"1985-12-1",2500,None,10))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()