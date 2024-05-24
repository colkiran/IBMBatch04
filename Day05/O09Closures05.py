
def fun(*args):
    print(*args)

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)

print("-" * 60)

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def logdetails(fnc):
    info = "Logging into the service....."

    def helper(*args):
        print(info)
        print(fnc(*args))
        print("-" * 60)

    return helper

sumlogger = logdetails(sum)
sumlogger(10, 20)