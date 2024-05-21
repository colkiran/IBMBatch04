"""
while loop executes until the condition is True

"""
i = 10
while i > 0:
    print(i, end=" ")
    i -= 1
print()

print(f"i :{i}")
print("-" * 60)

while(True):
    print(i, end=" ")
    i += 1
    if i > 10: break
