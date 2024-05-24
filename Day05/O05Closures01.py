
def outerFun():
    info = "Sachin"
    def innerFun():

        print("Hello World")
        print(f"info :{info}")

    return innerFun

inref = outerFun()
inref()

print("-" * 60)
outerFun()()            # calls the innerFun




# print("-" * 60)
# def add(x, y):
#     return x + y
#
# res = add(10, 20)
# print(res)
