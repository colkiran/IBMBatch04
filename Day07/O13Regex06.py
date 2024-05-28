
import re

st = "boat"

res = re.search(r'(boat|bait)', st)

if res:
    print("Match found....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found....")