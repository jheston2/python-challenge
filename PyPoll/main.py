import os
import csv

count = int()
df = []

csvpath = os.path.join("election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        df.append(row)

    for row in df:
        count += 1

print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {count}")
print(f"----------------------")