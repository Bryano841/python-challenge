import os
import csv
import statistics

finance_csv = os.path.join("C:\\Users\\bryan_j7mwyoj\\Desktop\\python-challenge\\03-Python_Homework_Instructions_Pybank_Resources_budget_data.csv")

with open(finance_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    sDecrease = 0
    sIncrease = 0
    pDecrease = 0
    pIncrease = 0
    pValue = 0
    tChange = 0

    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        if row_count > 1:
            if value > pValue:
                vIncrease = value - pValue
                tChange += vIncrease
                if vIncrease > sIncrease:
                    sIncrease = vIncrease
            elif value < pValue:
                vDecrease = pValue - value
                tChange +=  - vDecrease
                if vDecrease > sDecrease:
                    sDecrease = vDecrease

        pValue = value            
        totals.append(value)

change = tChange/(row_count - 1)

print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: {}".format(row_count))
print ("Total: {}".format(sum(totals)))
print ("Average Change: {}".format(change))
print ("Greatest Increase in Profits: {}".format(sIncrease))
print ("Greatest Decrease in Profits: {}".format(sDecrease * -1))



output_file = os.path.join("Analysis.txt")


with open(output_file, "w") as text_file:
    text_file.write ("Financial Analysis\n")
    text_file.write ("-------------------------------\n")
    text_file.write ("Total Months: {}\n".format(row_count))
    text_file.write("Total: {}\n".format(sum(totals)))
    text_file.write ("Average Change: {}\n".format(change))
    text_file.write ("Greatest Increase in Profits: {}\n".format(sIncrease))
    text_file.write("Greatest Decrease in Profits: {}\n".format(sDecrease * -1))


     