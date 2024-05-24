
def outerFun():
    info = "Sachin"
    def innerFun():

        print("Hello World")
        print(f"info :{info}")

    innerFun()

outerFun()
