# Read CSV file

import os
import csv

print("Financial Analysis")
print("--------------------------")

csvpath = os.path.join('Resources', 'budget_data.csv')

#calculate months
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    months = 0   
    for x in csvreader:
        months = months+1
    print (f"Total Months: {months}")

#calculate Profits
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    Profits = 0
    for row in csvreader:
        Profits = Profits + int(row[1]) 
    print (f"Total Profits: ${Profits}")

#calculate Change in profits 

MoM_Growth = []
ginc = ["", 0]
gdec = ["", 0]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    first_profit = next(csvreader)
    oldgrowth = int(first_profit[1])
    for month in csvreader:
       Growth = int(month[1]) - oldgrowth
       oldgrowth = int(month[1])
       MoM_Growth += [Growth]

# Calculate Gratest Increase and decrease
       if Growth > ginc[1]:
            ginc[0] = month[0]
            ginc[1] = Growth
        
       if Growth < gdec[1]:
            gdec[0] = month[0]
            gdec[1] = Growth

# Calculate average change in Profits 
Avg = sum(MoM_Growth) / len(MoM_Growth)


print(f"Average MoM Change : {Avg:.2f}")
print(f"Greatest Increase in Profits: ({ginc})")
print(f"Greatest Decrease in Profits: ({gdec})")

results = os.path.join("analysis","Bank_Analysis.txt")
Printer = open(results, "w")
Printer.write(f"""Financial Analysis PyBank
--------------------------------
Total Observed Months: {months}
Total Profits: ${Profits}
Average MoM Change : {Avg:.2f}
Greatest Increase in Profits: ({ginc})
Greatest Decrease in Profits: ({gdec})
""")