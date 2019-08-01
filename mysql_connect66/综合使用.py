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

    sql = "drop table t_emp_new"
    cursor.execute(sql)

    # sql="create table t_emp_new as (select * from t_emp)"
    sql = "create table t_emp_new like t_emp"  # 仅保留结构，无数据
    cursor.execute(sql)

    sql = "select avg(sal) as avg from t_emp"
    cursor.execute(sql)
    temp = cursor.fetchone()
    avg = temp[0]  # 公司的平均底薪

    sql = "select deptno from t_emp group by deptno having avg(sal)>=%s"
    cursor.execute(sql, [avg])
    # for one in cursor:
    #     print(one[0])
    temp = cursor.fetchall()  # 一次性把游标内的结果集取出来
    print(temp)

    sql = "insert into t_emp_new select * from t_emp where deptno in ("
    for index in range(len(temp)):
        one = temp[index][0]
        if index < len(temp) - 1:
            sql += str(one) + ","  # 转为字符串
        else:
            sql += str(one)
    sql += ")"
    print(sql)
    cursor.execute(sql)

    sql = "delete from t_emp where deptno in ("
    for index in range(len(temp)):
        one = temp[index][0]
        if index < len(temp) - 1:
            sql += str(one) + ","  # 转为字符串
        else:
            sql += str(one)
    sql += ")"
    print(sql)
    cursor.execute(sql)

    sql = "select deptno from t_dept where dname=%s"
    cursor.execute(sql, ["SALES"])
    deptno = cursor.fetchone()[0]
    sql = "update t_emp_new set deptno=%s"
    cursor.execute(sql, [deptno])

    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
# 无需关闭
