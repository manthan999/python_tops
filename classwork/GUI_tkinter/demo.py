from tkinter import *


root = Tk()
root.geometry("400x400")


# b = Button(root,text="submit").pack(side=LEFT)
# b = Button(root,text="submit").grid(row=1,column=1)
# b1 = Button(root,text="reset").grid(row=2,column=2)

l1 = Label(root,text="name").place(x =100,y = 50 )
l2 = Label(root,text="Eamil").place(x =100,y = 100 )
l3 = Label(root,text="Phone").place(x =100,y = 150 )

t1 = Entry(root).place(x = 160,y=50)
t2 = Entry(root).place(x = 160,y=100)
t3 = Entry(root).place(x = 160,y=150)

b = Button(root,text="submit").place(x=100,y=200)
b1 = Button(root,text="reset").place(x=200,y=200)


root.mainloop()