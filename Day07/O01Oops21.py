
from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's job......")


class Developer(Employee):

    def doJob(self):
        print("Developer's job.......")


def BankJob(emp):
    print(f"Bank job started....")
    emp.doJob()
    print(f"Bank job ended.......")
    print("-" * 60)

mike = Manager()
david = Developer()

BankJob(mike)
BankJob(david)


