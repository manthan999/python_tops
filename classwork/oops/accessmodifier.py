
class Test:

    a = 10
    _b = 50
    __c = 500
    def display(self):
        print("running display",self._a,self.__c)


t = Test()
t._a = 50
t._Test__c = 100
t.display()

# print(dir(t))