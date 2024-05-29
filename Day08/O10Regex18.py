"""
1. string that didn't match the regular expression
2. string that matched the regex
3. string that is not checked by regex
"""
import re

st = "the quick brown fox jumps over the lazy dog"

res = re.sub(r'fox',"tiger", st)

if res:
    print("Match found.....")
    print(f"res :{res}")
else:
    print("Match not found....")
