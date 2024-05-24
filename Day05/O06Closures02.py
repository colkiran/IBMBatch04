

def outerFun(flag):

    def innerFun1():
        print("Hello World")

    def innerFun2(gname):
        print(F"Greetings {gname}")

    if flag == 1:
        return innerFun1
    elif flag == 2:
        return innerFun2

inref = outerFun(2)
inref("Rahul")
#
# inref = outerFun(2)
# inref()

