import os
import csv

csvpath = os.path.join("budget_data.csv")
monthcount = int()
profitloss = float()
net = float()


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # for row in csvreader:
    #     print(row)

    csvheader = next(csvreader)
    for row in csvreader:
        monthcount += 1
        profitloss = float(row[1])
        net += profitloss
    print(monthcount)
    print(net)
    
