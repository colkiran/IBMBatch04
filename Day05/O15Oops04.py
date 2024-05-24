
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized........")

    def get_detials(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 32)
ply1.get_detials()

print("-" * 60)
ply2 = Player("Rahul", 30)
ply2.get_detials()

print("-" * 60)
print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 60)
ply2.runs = 150
print(ply2.__dict__)
print(ply1.__dict__)
