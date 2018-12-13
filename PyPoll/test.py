import os
import csv
import numpy as np

count = int()
df = []
candidates = []
candidates_unique = []
khancount = int()

# create list df
csvpath = os.path.join("election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        df.append(row)

# create list of candidates
candidates = [item[2] for item in df]

# create list of unique candidates
for x in candidates:
    if x not in candidates_unique:
        candidates_unique.append(x)

#count votes for each candidate
#candidate 1 - Khan
for x in candidates:
    if candidates == 'Khan':
        khancount += 1

print(head(candidates))