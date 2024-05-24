
class Player:

    def __init__(self):                 # constructor.....
        print('Player initialized.......')
    def get_runs(self):
        print("runs scored.....")

sachin = Player()       # calls the constructor
virat = Player()
sachin.__init__()

print("-" * 60)
sachin.get_runs()
virat.get_runs()
