
class A:

    def __init__(self):
        print("A calling")

    def display(self):
        print("Display calling")

class B(A) : 
    def __init__(self):
        print("B Calling")
        super().__init__()
        

    def sample(self):
        print("Sample calling")

# class C(B):
#     print("multilevel")

# class C(B,A):
#     print("multiple")

# class C(A):
#     print("Hirarchicle")

# b  = B()
# b.sample()
# b.display()




class Animal:

    a = 10
    def __init__(self,name):
        self.name=  name

    def voice(self):
        print("generic animal voice")


class Dog(Animal):
    a = 200
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print(self.name,self.breed,self.a)
    
    def voice(self):
       print("wow...wow")
       

class Cat(Animal):
    a = 100
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    
    def display(self):
        print(self.name,self.color,self.a)
    
    def voice(self):
        print("meaw...meaw")


d  =Dog("Tommy","lebra")
d.display()
d.voice()

c  =Cat("Pushpa","White")
c.display()
c.voice()