
glbx = 100

def fun(y):             # this is a local variable
    global glbx         # do not assign any value to the variable in this line
    print(f"y :{y}")
    glbx = 150
    print(f"glbx :{glbx}")


print(f"glbx before :{glbx}")

fun(25)

print(f"glbx after :{glbx}")
