
FL = open("data.txt", "rb")

pos = FL.seek(50, 0)
print(f"Position :{pos}")
print("-" * 60)

pos = FL.seek(75, 1)
print(f"Position :{pos}")
print("-" * 60)

pos = FL.seek(100, 2)
print(f"Position :{pos}")
print("-" * 60)

pos = FL.seek(0, 2)
print(f"Position :{pos}")
print("-" * 60)

pos = FL.seek(-500, 2)
print(f"Position :{pos}")
print("-" * 60)

# pos = FL.seek(-10, 0)
# print(f"Position :{pos}")
# print("-" * 60)

FL.close()
