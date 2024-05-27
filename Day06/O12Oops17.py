class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = 1

    def eat(self):
        print("animals eat")

class Bird(Animal):

    def __init__(self):
        super().__init__()             # calls the parent class ctor..
        print("Bird Ctor.....")
        self.size = '1 k'

    def fly(self):
        print("birds fly......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print(cuckoo.__dict__)
