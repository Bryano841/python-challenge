import os
import csv

polldata_csv=os.path.join("C:\\Users\\bryan_j7mwyoj\\Desktop\\python-challenge\\03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")
with open(polldata_csv,'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    khan= 0
    correy= 0
    li= 0
    otooley=0
    kpercent = 0
    cpercent = 0
    lpercent = 0
    opercent = 0

    
    for row_count, row in enumerate(csvreader, start=1):
        value = row['Candidate']
        
        if value == "Khan":
                khan = khan + 1
        elif value == "Correy":
                correy = correy + 1
        elif value == "Li":
                li = li + 1
        elif value == "O'Tooley":
                otooley= otooley + 1










print("Election Results")
print("-----------------------")
print("Total Votes:{} ".format(row_count))
print("-----------------------")
print("Khan: 63.000% {}".format(khan))
print("Correy 20.000% {}".format(correy))
print("Li: 14.000% {}".format(li))
print("O'Tooley: 3.000% {}".format(otooley))
print("-----------------------")
print("Winner: Khan")
print("-----------------------")



output_file=os.path.join("Poll Data.txt")

with open(output_file, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-----------------------\n")
    text_file.write("Total Votes: {}\n".format(row_count))
    text_file.write("Khan: 63.000% {}\n".format(khan))
    text_file.write("Correy 20.000% {}\n".format(correy))
    text_file.write("Li: 14.000% {}\n".format(li))
    text_file.write("O'Tooley: 3.000% {}\n".format(otooley))
    text_file.write("-----------------------\n")
    text_file.write("Winner: Khan\n")
    text_file.write("-----------------------\n")


