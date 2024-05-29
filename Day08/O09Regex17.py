
import re

st = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""

regex = re.compile('(t\w+)')
print(regex)
res = re.findall(regex, st)
print(f"res :{res}")
print(len(res))

print("-" * 60)
regex = re.compile('(t\w+)')
for match in re.finditer(regex, st):
    s = match.start()
    e = match.end()
    print(f"The string found between {s} and {e} :", st[s:e])
