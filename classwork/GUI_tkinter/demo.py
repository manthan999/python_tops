from tkinter import *
import mysql.connector as sql
from tkinter import messagebox

con = sql.connect(
    host="localhost",
    user="root",
    password="root",
    port = 3306,
    database = "27aug_python"
)

root = Tk()
root.geometry("400x400")

def adddata():
    name = t1.get()
    email = t2.get()
    phone = t3.get()
    cursor = con.cursor()
    qry = "insert into student values(%s,%s,%s,%s)"
    val = (0,name,email,phone)
    cursor.execute(qry,val)
    con.commit()
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    messagebox.showinfo("Success","Data inserted successfully !!!")
    

# b = Button(root,text="submit").pack(side=LEFT)
# b = Button(root,text="submit").grid(row=1,column=1)
# b1 = Button(root,text="reset").grid(row=2,column=2)

l1 = Label(root,text="Name").place(x =100,y = 50 )
l2 = Label(root,text="Eamil").place(x =100,y = 100 )
l3 = Label(root,text="Phone").place(x =100,y = 150 )

t1 = Entry(root)
t1.place(x = 160,y=50)
t2 = Entry(root)
t2.place(x = 160,y=100)
t3 = Entry(root)
t3.place(x = 160,y=150)

b = Button(root,text="submit",command=adddata).place(x=100,y=200)
b1 = Button(root,text="reset").place(x=200,y=200)


root.mainloop()