
def greet():
    print("Greetings Mr.Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event....")

# city is a default argument and gname is a non default argument
def greetGstCty(gname,  cty = "Mumbai"):
    print(f"Greetings Mr.{gname} from {cty}, Welcome to the event.....")


greet()

print("-" * 60)
greetGst("Rahul")
greetGst("Sachin")

print("-" * 60)
greetGstCty("Sunil")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
# Function can return values

def multiplyMe(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, multiplyMe(10, 20)))

# recursive calls

def fun(x):
    if x == 0:
        exit()
    print(x, end=" ")
    fun(x - 1)
print()

# fun(10)

print("-" * 60)
from collections import namedtuple

def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("Arith", "s d p q")
    arith = nmdTpl(s= sum, d = diff, p = prod, q = quot)
    return arith

res = arithCalc(30, 8)
print(f"res :{res}")
print(f"sum  :{res.s}")
print(f"diff :{res.d}")
print(f"prod :{res.p}")
print(f"quot :{res.q}")

print("-" * 60)
# variable length argument - *args, **kwargs

def prodAll(*numbers):
    print(numbers)
    print(*numbers)         # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(prodAll(1, 2, 3, 4, 5))

print("-" * 60)

def extractDet(**details):
    print(details)
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)

extractDet(name="Rahul", age=30, runs=150, oppn="Ban")

print("-" * 60)
def admsn(fn, ln, dob, gen, conno, pan, adhar, adr):
    print(f"Name    :{fn}{ln}")
    print(f"DOB     :{dob}")
    print(f"Gender  :{gen}")
    print(f"Con No. :{conno}")
    print(f"PAN     :{pan}")
    print(f"Adhar   :{adhar}")
    print(f"Address :{adr}")

admsn(pan='APERIIA234', dob="10/05/1993", adhar="23904092", fn='Jack', ln='Slater', gen="Male", adr="MG Road Bangalore", conno="9234882934")

print("-" * 60)

def fun1():
    # this is a comment
    "this is a doc string"
    print("Hello World")

fun1()
print(fun1.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1
    ----
    1. if x and y are integers then the result would the product of the numbers
    2. if x and y are text then the result would be the contcatenated string
    3. if x and y are different data types then the result would be an error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello", "world"))

help(fun1)