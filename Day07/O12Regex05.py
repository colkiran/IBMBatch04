
import re

st = "b8t"

# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[^aeiou]t', st)
res = re.search(r'b[a-zA-Z0-9]t', st)

if res:
    print("Match found....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found....")