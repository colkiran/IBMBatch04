
print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")

# convert the list into a dictionary
res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 22)
print(f"res :{res}")

print("setdefault".center(60, "-"))
# never allows to modify the existing key value, only adds a new key value
emp = {'ename': 'Kevin', 'age': 36, 'desig': "MGR"}
print(f"emp :{emp}")

emp.setdefault('ename', 'Costner')
emp.setdefault("desig", "GM")
emp.setdefault("dept", "MKT")
emp.setdefault("loc", 'Blr')

print(f"emp :{emp}")

print("pop".center(60, "-"))
emp = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd'}

print(f"emp :{emp}")

res = emp.pop('desig')
print(f'res :{res}')

res = emp.pop('loc')
print(f'res :{res}')

# res = emp.pop()
# print(f'res :{res}')

print(f"emp :{emp}")

print("popitem".center(60, "-"))
emp1 = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd'}

print(f"emp1 :{emp1}")

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

print(f"emp1 :{emp1}")

print("update".center(60,  "-"))

emp1 =  {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male'}

emp2 =  {'ename': 'Micheal', 'age': 32, 'gender': 'male', 'loc': 'blr'}

print(f"emp1 :{emp1}")

print("-" * 60)

print(f"emp2 :{emp2}")

# modify emp1's values with emp2

emp1.update(emp2)
print(f"emp1 :{emp1}")