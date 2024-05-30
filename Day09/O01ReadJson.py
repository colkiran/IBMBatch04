
import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k,v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("-" * 60)
# data should be enclosed in single quote(')
empdata = '{"name": "Micheal", "age": 29, "city": "California"}'

print(empdata)
print(type(empdata))

res = json.loads(empdata)
print(type(res))
for k, v in res.items():
    print(k, "=>", v)

# load is used to read the json document from a file
# loads is used to convert JSON string to python dictionary