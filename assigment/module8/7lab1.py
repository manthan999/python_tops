# simple inheritance
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

# multilevel inheritance
class C(B):
    print("multilevel")

# # multiple inheritance
# class C(B,A):
#     print("multiple")

b  = B()
b.sample()
b.display()