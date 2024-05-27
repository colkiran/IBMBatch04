import lib2to3.pytree


class Player:

    def __init__(self, name, age):
        print(f"Player Ctor.....")
        self.name = name
        self.age = age

    def get_detials(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("Factory......")
        return cls(f"{fn} {ln}", age)    # calls the constructor


ply1 = Player('Virat', 28)      # constructor will get called

print("-" * 60)
ply2 = Player.CreatePlayer("Rohit", "Sharma", 31)
ply2.get_detials()
