
# clear

emp = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd'}

print(f"emp :{emp}")
emp.clear()

print(f"emp :{emp}")

print("copy".center(60, "-"))
emp1 = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd'}

print(f"emp1 before:{emp1}")
# copy emp1 into emp2

emp2 = emp1         # shallow copy
print(f"emp2 before :{emp2}")

emp2['dept'] = 'MKT'
emp2['salary'] = 35000

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)
emp3 = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd'}

print(f"emp3 before :{emp3}")
# copy emp3 into emp4

emp4 = emp3.copy()
print(f"emp4 before :{emp4}")

emp4['dept'] = 'MKT'
emp4['salary'] = 35000

print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("=" * 60)
emp5 = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd', 'salary': {'hp': 20000, 'TCS': 35000}}
print(f"emp5 before :{emp5}")
# copy emp5 into emp6

emp6 = emp5.copy()
print(f"emp6 before :{emp6}")

emp6['salary']['hcl'] = 50000
emp6['salary']['genpact'] = 75000

print(f"emp6 after :{emp6}")
print(f"emp5 after :{emp5}")

print("=" * 60)
from copy import deepcopy
emp7 = {'ename': 'Kevin', 'age': 36, 'desig': "MGR", 'gender': 'male', 'loc': 'hyd', 'salary': {'hp': 20000, 'TCS': 35000}}
print(f"emp7 before :{emp7}")

# copy emp7 into emp8

emp8 = deepcopy(emp7)
print(f"emp8  before :{emp8}")

emp8['salary']['hcl'] = 50000
emp8['salary']['genpact'] = 75000

print(f"emp8 after :{emp8}")
print(f"emp7 after :{emp7}")
