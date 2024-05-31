
import threading
import time

def doJob(secs, tname):
    print(f"function going to sleep.....{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up....{threading.current_thread().name}")

s = time.perf_counter()

threads = []

for i in range(500):
    t = threading.Thread(target=doJob, name="t"+str(i), args=[2, "t"+str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

e =time.perf_counter()
print(f"the total time taken is {round(e -s, 2)}")
