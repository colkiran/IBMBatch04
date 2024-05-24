
def outerFun(greet):
    def innerFun(gname):

        print(greet, gname)

    return innerFun
# simple curry
engGrt = outerFun("Welcome")
kanGrt = outerFun("Namaskara")

engGrt("Virat")
engGrt("Sachin")
kanGrt("Kumble")