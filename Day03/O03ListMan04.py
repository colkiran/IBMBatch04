"""
sort    -   sort function will sort the original list
sorted  -   sorted function will take a copy of the list sort it and                return it
"""

l1 = [10, 7, 2, 8, 6, 1, 9, 3, 4, 5]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending  :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 60)
l1 = [10, "zebra", "apple", 7, "yellow", "blue", 2, 'white', 'green',  8, "pink", 'violet', 6, 'cat', 'dog', 1, 'orange', 'jemlems',  9, 3, 4, 5, 128, 1045, 29, 249, 2013]

print(f"l1 :{l1}")
res = sorted(l1, key=ascii)
print("-" * 60)
print(f"res :{res}")

idx = 0
for i in range(len(res)):
    if type(res[i]) == int:
        idx = i
        break
print(f"res[idx] :{res[idx]}")

print("-" * 60)
print(res[:idx] + sorted(res[idx:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'ooty', 'bangalore', 'delhi', 'chennai', 'pune', 'hyderabad', 'vishakapatnam', 'kolkotta']
print(f"cities :{cities}")

print("-" * 60)
# sort the cities by their length
res  = sorted(cities, key=len)
print(f"res :{res}")

