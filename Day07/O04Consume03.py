
import sys

# print(sys.path)
sys.path.append("C:/Delhi")

for path in sys.path:
    print(path)

import gurgaon.mymodule as m

m.greet("Rahul")
