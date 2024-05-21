
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print("find".center(60, "-"))
print(f"st1 :{st1}")

pos = st1.find("w")
print(f"Index :{pos}")

pos = st1.find("l")
print(f"Index of 1st l :{pos}")

# st1 = "abclsdsalasassalasasa"
# hard coding
pos = st1.find("l", 6)
print(f"Index of 3rd l :{pos}")

# generic code
pos = st1.find("l", st1.find("l") + 1)
print(f"Index of 2nd l :{pos}")

pos = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"Index of 3rd l :{pos}")

print("-" * 60)
print(f"st2 :{st2}")
print(st2.find("fox"))

pos = st2.find("the")
print(f"1st index :{pos}")

pos = st2.find("the", st2.find("the") + 1)
print(f"2nd index :{pos}")

print("replace".center(60, "-"))
print(f"st1: {st1}")

res = st1.replace("h", "H")
print(f"res :{res}")

res = st1.replace("l", "L",2)
print(f"res :{res}")

print("-" * 60)
print(f"st2 :{st2}")
res = st2.replace("fox", "tiger")

print(f"res :{res}")

res = st2.replace("the", "The", 1)
print(f"res :{res}")

print("-" * 60)
st = "*****hello*****"
print(f"st :{st}")

print(f"left  :{st.lstrip('*')}")
print(f"right :{st.rstrip('*')}")
print(f"both  :{st.strip('*')}")

print("-" * 60)
# maketrans and translate
st = 'hello world'
a = 'helowrd'
b = 'HELOWRD'
print(f"st :{st}")
# the length of a and b should be the same
resTbl = st.maketrans(a, b)
print(resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

