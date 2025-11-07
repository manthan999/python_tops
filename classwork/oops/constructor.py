class Student:

    clg = "tops"
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email=email

    def display(self):
        print(self.id,self.name,self.email,self.clg)

    @classmethod
    def test(cls):
        
        print("test calling"+cls.clg)

    @staticmethod
    def run():
        print("run calling")


# Student.test()        

# Student.clg="T"
# Student.test()

s = Student(10,'Krish',"krish@gmail.com")
s.display()
s.test()


# s1 = Student(11,"ranjeet","ranjit@gmail.com")
# s1.display()

# Student.run()