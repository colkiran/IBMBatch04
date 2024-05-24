
def outerFun():
    gname = "Rahul"
    def innerFun():
        nonlocal gname
        gname = "Mr." + gname
        print("Hello World")
        print(f"Welcome {gname}")

    innerFun()
    print(f"outer :{gname}")

outerFun()

