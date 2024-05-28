
import re

st = "b*t"

res = re.match(r'b.t', st)

if res:
    print("Match found....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found....")