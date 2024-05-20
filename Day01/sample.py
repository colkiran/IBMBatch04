#!  c:\python\bin

print("Hello World")
# this is a comment
print("Hello World")      # this is a comment

"""
print("Hello World")
print("Hello World")
print("Hello World")
"""

print("-" * 60)
def fun():
    # function code
    print("hello world")
    for i in range(1, 31):
        # for loop code
        if i % 2 == 1:
            # if condition code
            continue        # skip the iteration

        print(i)
    # function code
    print("hello world")

fun()

