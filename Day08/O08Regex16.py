"""
1. string that didn't match the regular expression
2. string that matched the regex
3. string that is not checked by regex
"""
import re

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'fox', st)

if res:
    print("Match found.....")
    print("String that didn't match regex :",st[:res.start()])
    print("String that matched Regex :", res.group(0))
    print("String that is not checked by regex :", st[res.end():])
else:
    print("Match not found....")
