
from calendar import month_abbr

months = ['dec', 'jun', 'aug', 'nov', 'oct', 'apr', 'mar', 'sep', 'jan', 'jul', 'may', 'feb']
print(f"unsorted months :{months}")

print("-" * 60)

print(f"month_abbr :{list(month_abbr)}")

print("-" * 60)

res = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(f"Sorted Months :{res}")
