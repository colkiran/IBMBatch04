"""
read()  - entire content of the file
read(no of bytes) - reads the no of bytes spefied from the file.
-----------------------------------------
readline() - reads one line and stores it in the buffer
readline(no of bytes) - specify it less than the buffered data
"""


FL = open("data.txt", "r")

# st = FL.read(500)
# print(st)
print("-" * 60)
# st = FL.readline(950)
# print(st)
print("-" * 60)
# st = FL.readlines()
# print(st)

# for line in FL.readlines():
#     print(line)

st = FL.readlines()
print("Length ", len(st))
FL.close()