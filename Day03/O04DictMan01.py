
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'age': 32, 'runs': 86, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'virat'), ('age', 30), ('runs', 135), ('oppn', 'eng')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='rohit', age=32, runs=89, oppn="WI")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD
player = {'name': 'sachin', 'age': 30, 'runs': 98, 'oppn': 'WI'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
# iterate
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# updation - modification, adding new key value
print(f"player :{player}")
player['name'] = "tendulkar"
player['age'] = 24
player['year'] = 1995
player['venue'] = 'Sabina Park'

print(f"player :{player}")

print("-" * 60)
# deletion
del player['age']
del player['oppn']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
