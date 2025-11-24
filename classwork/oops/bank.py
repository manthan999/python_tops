from abc import ABC,abstractmethod

class Account(ABC):

    balance = 0
    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdrow(self,amount):
        pass

    def checkbalance(self):
        print("current balance is : ",self.balance)


class SavingAccount(Account):

    def deposite(self, amount):
        self.balance=self.balance+amount
    
    def withdrow(self, amount):
        if amount>self.balance:
            print("Insufficient amount")
        else:
            self.balance = self.balance-amount




s  =SavingAccount()
s.checkbalance()
s.deposite(5000)
s.deposite(15000)
s.checkbalance()
s.withdrow(2000)
s.checkbalance()