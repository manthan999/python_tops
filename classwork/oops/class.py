# The class `Pen` defines attributes such as price, color, and company, and includes a method
# `to_write` that prints "something".
class Pen:

    price = 20
    color = "Red"
    company="Cello"

    def to_write(self):
        print("something")
        print(self.price,self.color,self.company)
        
p = Pen()
p.price=100
p.to_write()

p1 = Pen()
p1.to_write()