
import re

st = "baaaaaaaaaaaaaaaaaaat"

# res = re.search(r'ba*t', st)
# res = re.search(r'ba?t', st)
res = re.search(r'ba+t', st)


if res:
    print("Match found....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found....")