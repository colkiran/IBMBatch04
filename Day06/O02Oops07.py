
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

ply1 = Player("Sachin", 32)
# ply1.get_details()
# a = 10
# print(a, "\t", str(a))

print("-" * 60)
print(str(ply1))
