
# l1 = []
# print(dir(l1))

print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

# 10, 11, 12
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("extend".center(60, "-"))
l2 = [6, 7, 8, 9, 10]
print(f"l2 :{l2}")

l2.extend([11, 12, 13])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = list(range(5, 36, 5))
print(f"l1 :{l1}")
l1.insert(1, 6)
l1.insert(2, 7)
#-----------------------------
l1.insert(0, 1)
l1.insert(1, 2)
l1.insert(2, 3)
#-----------------------------
l1.insert(14, 36)
l1.insert(15, 37)
l1.insert(16, 38)

print(f"l1 :{l1}")
''
print("pop".center(60, "-"))
l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()      # removes the last element
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

l1.remove(3)
l1.remove(3)
l1.remove(3)

print(f"l1 :{l1}")
print("-" * 60)

while 2 in l1:
    l1.remove(2)

print(l1)

print("clear".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1.clear()

print(f"l1 :{l1}")
