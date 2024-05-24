# HOF - any function if it takes another function as an argument or return a function as a reference

def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

engGrt = outerFun("Welcome")
engGrtTgr = engGrt("bear")

engGrtTgr("Prabhakar")

"""
engGrt = outerFun("Welcome")
engGrtSngArw = engGrt("------>")
kanGrt = outerFun("Namaskara")
kanGrtDblArw = kanGrt("======>")

engGrtSngArw("Virat")
kanGrtDblArw("Rahul")
"""
