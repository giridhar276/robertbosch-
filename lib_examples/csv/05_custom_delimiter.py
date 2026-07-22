import csv
with open("pipe_data.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["A", "B", "C"])
    writer.writerow([1, 2, 3])
with open("pipe_data.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        print(row)
