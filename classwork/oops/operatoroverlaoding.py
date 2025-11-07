class Calc:

    def __init__(self,a,b,c):
        self.a = a
        self.b  = b
        self.c = c

    def __add__(self,obj):
        return self.a+obj.a,self.b+obj.b,self.c+obj.c
    
    def __mul__(self,obj):
        return self.a*obj.a,self.b*obj.b,self.c*obj.c


c1 = Calc(10,20,30)
c2 = Calc(30,40,50)

k = c1+c2
print(k)

m = c1*c2
print(m)