

import re

st = "hello world"

# match will match only at the beginning of the string
# res = re.match(r'^hello', st)
res = re.search(r'world$', st)

if res:
    print("Match found....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found....")