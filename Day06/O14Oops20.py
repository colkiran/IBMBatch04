
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def deposit(self):
        print("Amount #####.## credited into the account....")

    def getBalance(self):
        print("Balance in the account is ######.##")

sav1 = Savings()
sav1.deposit()
sav1.getBalance()