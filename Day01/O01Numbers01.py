
"""
int
float
complex
"""

a = 100
b = -100

print(f"a :{a}")    # f string or format string used for interpolation
print(type(a))      # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-"  * 60)
c = 100.5
d = -100.5

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-"  * 60)

e = +2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-"  * 60)
g = 10 + 3j
h = 10 - 3j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-"  * 60)

print("Max :", max(78, 23, 65, 17, 46, 82, 30))
print("Min :", min(78, 23, 65, 17, 46, 82, 30))

print("-"  * 60)

x = 2 + 3.5
print(type(x))

x = 3
y = 2.5
z = x + y

print("x = ", type(x))
print("y = ", type(y))
print("z = ", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System Conversion".center(60, "-"))
a = 50
print(oct(a))
print(hex(a))
print(bin(a))
