from multipledispatch import dispatch
class Calc:

    @dispatch(int, int)
    def add(self,a,b):
        print(a+b)

    @dispatch(int, int,int)
    def add(self,a,b,c):
        print(a+b+c)



c = Calc()
c.add(10,20)
c.add(10,20,30)