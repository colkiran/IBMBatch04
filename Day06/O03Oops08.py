
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # if we are overloading __eq__ operator then __ne__ also will work
    def __eq__(self, other):
        return self.salary == other.salary

    # if we overload __gt__ it will also overload __lt__
    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Jack", 28000)
print(emp1)         # implicitly calls __str__ method
print("-" * 60)

emp2 = Employee("James", 30000)
print(emp2)
print("-" * 60)

# compares the address by default
if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

if emp1 < emp2:
    print("{}'s salary of {} is less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is NOT less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
print(emp1 >= emp2)
print(emp1 <= emp2)