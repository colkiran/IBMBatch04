
class Animal:

    def eat(self):
        print("animals eat......")

class Bird(Animal):

    def fly(self):
        print("birds fly.......")


class Chicken(Bird):

    def msg(self):
        print("Chickens are breeded for consumption....")

    def fly(self):
        print("Chickens seldom fly......")

chic = Chicken()
chic.msg()
chic.fly()
chic.eat()
