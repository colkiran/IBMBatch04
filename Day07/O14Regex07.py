
import re

st = "sample.py"

res = re.search(r'\.py', st)

if res:
    print("Match found....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found....")