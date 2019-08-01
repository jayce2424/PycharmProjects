import mysql.connector
config={
    "host":"192.168.10.200",
    "port":"3306",
    "user":"app",
    "password":"app123",
    "database":"vega"
}
con=mysql.connector.connect(**config)
username="1 or 1=1"
password="1 or 1=1"
sql="select count(*) from t_user where username=%s "\
    " and aes_decrypt(unhex(password),'HelloWorld')=%s";
cursor=con.cursor()
# cursor.execute(sql%(username,password))
cursor.execute(sql,(username,password))  #成功抵御sql注入：提前把sql先编译成二进制的sql，再传入数据，再次执行，省去做磁法分析和优化
print(cursor.fetchone()[0])   #预编译机制  向占位符传入数据，被当做普通数据，不会再做磁法分析，当做普通字符串
con.close()