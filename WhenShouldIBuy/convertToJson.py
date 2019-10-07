import json

with open('data.txt') as json_file:
    data = json.load(json_file,)

print(json.dumps(data, indent=4))
# print(data)
