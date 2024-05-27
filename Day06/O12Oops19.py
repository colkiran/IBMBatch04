
class Animal:

    def __init__(self):
        print("animal Ctor.....")
        self.a = 10

    def eat(self):
        print("animals eat....")

    def fun(self):
        print("Animal class fun method.....")

class Person:

    def __init__(self):
        print("person Ctor......")
        self.p = 20

    def talk(self):
        print("person talks......")

    def fun(self):
        print("Person class fun method....")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()              # calls the parent class Ctor
        Person.__init__(self)
        print("Girl Ctor.......")
        self.g = 30

    def walk(self):
        print("girls walk......")


tina = Girl()
tina.eat()
tina.talk()
tina.walk()
tina.fun()

print("-" * 60)
print(tina.__dict__)
