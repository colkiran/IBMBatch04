
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\n Salary is {self.salary}"

    def __add__(self, other):
        return Employee("Noname", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("Noname", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("Noname", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("Noname", self.salary / other.salary)

    def __floordiv__(self, other):
        return Employee("Noname", self.salary // other.salary)


emp1 = Employee('danny', 45000)
print(emp1)

print('-' * 60)
emp2 = Employee("Kevin" , 40000)
print(emp2)

print('-' * 60)
print(emp1 + emp2)

print('-' * 60)
emp4 = emp1 - emp2
print(emp4)

print('-' * 60)
emp5 = emp1 * emp2
print(emp5)

print('-' * 60)
emp6 = emp1 / emp2
print(emp6)

print('-' * 60)
emp7 = emp1 // emp2
print(emp7)



print('=' * 60)

emp3 = emp1 + emp2 + emp1 + emp2
print(emp3)



