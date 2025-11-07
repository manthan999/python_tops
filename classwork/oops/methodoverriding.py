class A:
    def display(self):
        print("A display calling")


class B(A):
    def display(self):
        print("B calling")
        # return super().display()

b  =B()
b.display()