# First we import the Module, this will allow us to create a file path 
import os
# import the module for reading csv files
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

with open (budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
#we are printing out the header of the csv file
    csv_header_budget = next(csv_file)


#There are 2 rows in the csv file and we are going to designate them as month and money
    months = 0
    money = 0
    pre_rev = 0
    total_ch = 0
    inc = ["",0]
    ind = ["", 0]
    #make a while loop to loop though the csv file 
    for row in csv_reader:
        months += 1
        rev = int(row[1])
        money += rev

        change = rev - pre_rev

        if pre_rev == 0:
            change = 0

        total_ch += change

        # Greatest increase
        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        # greatest LOSS
        if change < ind[1]:
            ind[0] = row[0]
            ind[1] = change

        pre_rev = rev



output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${money:,}
    Average Change: ${total_ch/(months-1):,.2f}
    Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
    Greatest Decrease in Profits: {ind[0]} (${ind[1]:,})
'''

print(output)

with open("output.txt", "w") as f:
  print(output, file=f)


