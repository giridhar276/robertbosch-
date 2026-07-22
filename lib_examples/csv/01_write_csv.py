import csv
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "NY"])
    writer.writerow(["Bob", 25, "LA"])
print("CSV file written")
