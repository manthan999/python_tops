from abc import ABC,abstractmethod

class Demo(ABC):

    @abstractmethod
    def test(self):
        pass


class Sample(Demo):

    def test(self):
        print("Test calling")
# d = Demo()
# d.test()

s = Sample()
s.test()