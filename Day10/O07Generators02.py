
def fun():
    x = 1
    print("Apples from Ooty....")
    yield x
    x += 9
    print("Oranges from kanpur....")
    yield x
    x += 10
    print("Grapes from hubli")
    yield x

res = fun()
print(res)

print("-" * 60)
print(next(res))

print("-" * 60)
print(next(res))

print("-" * 60)
print(next(res))

# print("-" * 60)
# print(next(res))

