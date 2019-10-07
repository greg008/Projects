import json
import csv

with open('data.txt') as json_file:
    data = json.load(json_file)


with open("data.csv", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['date'], item['lowestPrice']])

print(csv_file)

# print(json.dumps(data, indent=4))
# print(data)
