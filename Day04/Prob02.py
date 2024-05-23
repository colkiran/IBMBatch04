from pprint import pprint

dm = int(input("Enter the dimension of the matrix :"))

print(dm)

mat = []
for i in range(dm):
    temp = []
    for j in range(dm):
        if i == j:
            temp.append(1)
        else:
            temp.append(0)
    mat.append(temp)

print("-" * 60)
for i in mat:
    print(i)

