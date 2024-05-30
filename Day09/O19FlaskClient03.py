import json

import requests

print("get".center(60, "-"))

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/pepsi")

res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("=" * 60)
print("put".center(60, "-"))

response = requests.put(BASE + "getproduct/pepsi", data = {'cat': 'baverage'})
res = response.json()

print(res)
print("=" * 60)
for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("=" * 60)
print("patch".center(60, "-"))

data = {'price': 5000}
response = requests.patch(BASE + 'getproduct/coke', json = json.dumps(data))
res = response.json()

print(res)

