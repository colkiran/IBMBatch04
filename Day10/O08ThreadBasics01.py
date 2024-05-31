
# Executing the code sequentially or synchronously
import time
def fun():
    print("function going to sleep....")
    time.sleep(2)
    print("function just woke up......")

s = time.perf_counter()

fun()
fun()
fun()

e = time.perf_counter()

print(f"The total time taken to execute is {round(e - s, 2)}")
