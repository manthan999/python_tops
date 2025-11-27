import mysql.connector as sql


con = sql.connect(
    host="localhost",
    user="root",
    password="root",
    port = 3306,
    # database = "27aug_python"
)

cursor = con.cursor()

cursor.execute("create database 27aug_python")

cursor.execute("create table student(id int primary key auto_increment,name varchar(20),email varchar(50),phone varchar(15))")

cursor.execute("insert into student values(0,'manthon','manthan@gmail.com','7485968574')")

# qry = "insert into student values(%s,%s,%s,%s)"
# val = (0,'meet','meet@gmail.com','7452635241')
# cursor.execute(qry,val)
# con.commit()