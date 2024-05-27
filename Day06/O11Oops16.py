
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = 1

    def eat(self):
        print("animals eat")


class Bird(Animal):

    def fly(self):
        print("birds fly.....")

class Fish(Animal):

    def swim(self):
        print("fishes swim.....")


cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()
print(cuckoo.__dict__)

print("-" * 60)
dolphin = Fish()
dolphin.eat()
dolphin.swim()
print(dolphin.__dict__)

print("-" * 60)
print(isinstance(cuckoo, Bird))
print(isinstance(cuckoo, Animal))
print("-" * 60)
print(issubclass(Bird, Animal))
print(issubclass(Bird, object))
print(issubclass(Bird, Fish))

