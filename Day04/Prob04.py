
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))

iter  = int(input("Enter the fibo series to be generated :"))
print("fibonacci series")
for i in range(iter):
    print(fibo(i), end=" ")
print()


