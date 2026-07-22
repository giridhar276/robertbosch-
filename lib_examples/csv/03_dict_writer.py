import csv
data = [{"Name": "Charlie", "Age": 22}, {"Name": "Dana", "Age": 28}]
with open("dict_people.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age"])
    writer.writeheader()
    writer.writerows(data)
print("DictWriter CSV written")
