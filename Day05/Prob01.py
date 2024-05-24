
import time

def timeCalc(fnc):

    def helper(x):
        print("funtion execution strated......")
        st = time.perf_counter()
        fnc(x)
        et = time.perf_counter()
        print("function execution completed.....")
        print(f"The time taken to execute the function :{round(et - st, 2)}")

    return helper


@timeCalc
def fun(cntr):
    lst = []
    for i in range(cntr):
        for j in range(1, i + 1):
            lst.append(j ** 3)

fun(5500)
