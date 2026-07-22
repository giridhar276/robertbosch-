import csv
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
