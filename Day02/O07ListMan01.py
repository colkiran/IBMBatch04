
l1 = list()
print(f'l1 :{l1}')
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4.1, 5.2, 6.5, 7 + 1j, 8 - 3j, True, False, 'Ten', 'Eleven', 'Twelve']
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")

# iterate
for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
# update -> modification or insert new values
# modified
l1[2] = 300

# added as a new element
l1[1] = 150

# l1[5] = 10
print(f"l1 :{l1}")
# list are static not dynamic
print("-" * 60)
# delete
del l1[3]
del l1[1]
print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))
