

print("keys".center(60,"-"))
player = {'name': 'tendulkar', 'age': 24, 'runs': 98, 'oppn': 'WI', 'year': 1995, 'venue': 'Sabina Park'}
print(f"player :{player}")

kys = player.keys()
print(f"keys :{kys}")

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60, "-"))
player = {'name': 'tendulkar', 'age': 24, 'runs': 98, 'oppn': 'WI', 'year': 1995, 'venue': 'Sabina Park'}
print(f"player :{player}")

vl = player.values()
print(f"values :{vl}")

for vl in player.values():
    print(vl, end=" ")
print()

print("items".center(60, "-"))
# items = keys + values

emp = {
    'emp1': {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd'},
    'emp2': {'ename': 'Micheal', 'age': 32, 'desig': "TL", 'gender': 'male', 'loc': 'blr'},
    'emp3': {'ename': 'Aliyah', 'age': 30, 'desig': "BDE", 'gender': 'female', 'loc': 'che'}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")
print("-" * 60)
print(f"emp2 :{emp['emp2']}")
print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("get".center(60, "-"))
emp1 = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd'}
print(f"emp1 :{emp1}")

print("-" * 60)
print(f"Name  :{emp1.get('ename', 'Invalid Key, please enter a valid key.....')}")
print(f"Desig :{emp1.get('desi', 'Invalid Key, please enter a valid key.....')}")
