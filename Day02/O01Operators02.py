
print("Comparison Operator".center(60, '-'))
# ==, >, <, >=, <=, !=

print(f"1 == 1 :{1 == 1}")
print(f"1 == 2 :{1 == 2}")

a = 10
b = 15

print(f"a > b :{a > b}")
print(f"a < b :{a < b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(60, "-"))
# and, or , not
a = 10
b = 20

# and
print(f"a == a and b == b :{a == a and b == b}")
print(f"a == a and b == a :{a == a and b == a}")

print("-" * 60)
# or
print(f"a == a or a == b :{a == a or a == b}")
print(f"a == b or b == a :{a == b or b == a}")

print("-" * 60)
#not

print(f"not(a == a or a == b) :{not(a == a or a == b)}")
print(f"not(a == b or b == a) :{not(a == b or b == a)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")    # integer representation of unicode character
print(f"ord('z') :{ord('z')}")

print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("Bitwise Operator".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")

print(f"5 >> 1 :{5 >> 1}")
print(f"16 >> 1 :{16 >> 1}")

print("-" * 60)
# ternary operator
age = 19
print("Eligible" if age > 18 else "Not Eligible")
