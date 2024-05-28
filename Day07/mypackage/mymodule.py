
gstname = "Kapil Dev"

runs = {'pak': 2850, 'srilanka': 3459,'Aus': 2600}

player = ['sunil Gavaskar', 'Kapli Dev', "Mohindar Amarnath","Roger Binny", 'Srikanth']

def greet(gstname):
    print(f"Greetings {gstname} Welcome to the event......")
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

# print("Module Name :", __name__)

if __name__ == '__main__':

    print(f"gstname :{gstname}")

    greet("Gavaskar")

    ply1 = Player("Virat Kholi", "30")
    print(ply1)




