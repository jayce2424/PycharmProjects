# 把部门平均底薪超过公司平均底薪这样部门里的员工移入t_emp_new,并隶属于sales
import mysql.connector.pooling

config = {
    "host": "192.168.10.200",
    "port": 3306,
    "user": "app",
    "password": "app123",
    "database": "jqx"
}
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()

    sql = "insert into t_dept "\
          "(select max(deptno)+10,%s,%s from t_dept UNION "\
          "select max(deptno)+20,%s,%s from t_dept)"


    print(sql)
    cursor.execute(sql,("A部门A", "背景", "B部门B", "时海"))

    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
