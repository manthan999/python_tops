import sqlite3

con = sqlite3.connect("mydb.db")

# q = "create table student(id int primary key,name varchar(20),email char(50))"

# q = "insert into student values(3,'Manthon','monthon@gmail.com')"

# q = "update student set name='manthon puniwala', email='mp@gmail.com' where id=3"

# q = "delete from student where id=3"

# con.execute(q) 
# con.commit() 

data = con.execute("select * from student")
for i in data.fetchmany(size=3):
    print(i)