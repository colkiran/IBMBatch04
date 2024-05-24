
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 29
        print("Player Initialized........")

    def get_detials(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player()
ply1.get_detials()

print("-" * 60)

ply2 = Player()
ply2.name = "Sourav"
ply2.age = 32
ply2.get_detials()