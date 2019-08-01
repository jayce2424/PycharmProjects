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
sql="select count(*) from t_user where username="+username+\
    " and aes_decrypt(unhex(password),'HelloWorld')="+password;
cursor=con.cursor()
cursor.execute(sql)
print(cursor.fetchone()[0])
con.close()