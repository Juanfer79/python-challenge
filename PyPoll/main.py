

import os
import csv

print(f"""
Election Results
----------------------------

""")

votes=0
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for x in csvreader:
        votes = votes+1
    print (f"Total Votes {votes}")
print("--------------------------")

kvotes=0
Candidate1 = "Khan"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        if row[2] == Candidate1:
            kvotes = kvotes+1
    kpercent = kvotes/votes*100
    print (f"Khan: {kpercent:.3f} % ({kvotes})")


cvotes=0
Candidate2 = "Correy"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        if row[2] == Candidate2:
            cvotes = cvotes+1
    cpercent = cvotes/votes*100
    print (f"Correy: {cpercent:.3f} % ({cvotes})")

lvotes=0
Candidate3 = "Li"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        if row[2] == Candidate3:
            lvotes = lvotes+1
    lpercent = lvotes/votes*100
    print (f"Li: {lpercent:.3f} % ({lvotes})")

ovotes=0
Candidate4 = "O'Tooley"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        if row[2] == Candidate4:
            ovotes = ovotes+1
    opercent = ovotes/votes*100
    print (f"O'Tooley: {opercent:.3f} % ({ovotes})")


print("--------------------------")

if (kvotes > cvotes) and (kvotes > lvotes) and (kvotes > ovotes):
    Winner = "Khan"
elif (cvotes > kvotes) and (cvotes > lvotes) and (cvotes > ovotes):
    Winner = "Corey"
elif (lvotes > kvotes) and (lvotes > cvotes) and (lvotes > ovotes):
    Winner = "Li"
elif (ovotes > kvotes) and (ovotes > lvotes) and (ovotes > cvotes):
    Winner = "O Tooly"
else:
    Winner = "No Winner"
print(f"Winner: {Winner}")
    

print("--------------------------")


results = os.path.join("analysis","Poll_Analysis.txt")
Printer = open(results, "w")
Printer.write(f"""
Election Results
----------------------------
Total Votes {votes}
--------------------------
Khan: {kpercent:.3f} % ({kvotes})
Correy: {cpercent:.3f} % ({cvotes})
Li: {lpercent:.3f} % ({lvotes})
O'Tooley: {opercent:.3f} % ({ovotes})
--------------------------
Winner: {Winner}
--------------------------
""")

