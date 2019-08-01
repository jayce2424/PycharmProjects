#预先创建出一些数据库连接，然后缓存起来，避免了程序语言反复创建和销毁连接TCP协议三次握手
import mysql.connector.pooling
config={
    "host":"192.168.10.200",
    "port":3306,
    "user":"app",
    "password":"app123",
    "database":"jqx"
}
try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con=pool.get_connection()
    con.start_transaction()
    cursor=con.cursor()
    sql="update t_emp set sal=sal+%s where deptno=%s"
    cursor.execute(sql,(200,20))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
#无需关闭