
import threading
import time

def doJob():
    print(f"Function going to sleep :{threading.current_thread().name}")
    time.sleep(2)
    print(f"Function just woke up...:{threading.current_thread().name}")

thrd1 = threading.Thread(target=doJob, name="t1")
thrd2 = threading.Thread(target=doJob, name="t2")
thrd3 = threading.Thread(target=doJob, name="t3")

s = time.perf_counter()

thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()
thrd2.join()
thrd3.join()

e = time.perf_counter()
print(f"Total time taken to execute is {round(e - s, 2)}")
