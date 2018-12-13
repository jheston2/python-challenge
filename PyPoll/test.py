import os
import csv

count = int()

csvpath = os.path.join("election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    for row in csvreader:
        
        count +=1

print(count)