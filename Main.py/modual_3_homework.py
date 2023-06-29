# First we import the Module, this will allow us to create a file path 
import os
# import the module for reading csv files
import csv

budget_csv = os.path.join('budget_data.csv')

with open (budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
#we are printing out the header of the csv file
    csv_header_budget = next(csv_file)
    print(f"Header: {csv_header_budget}")


#There are 2 rows in the csv file and we are going to designate them as month and money
months = int(budget_csv[0])
money = int(budget_csv[1])
#make a while loop to loop though the csv file 
for row in csv_reader:
        #this will print the total number of months
        print(f'total months: len(months)')
        #this will print the total money added together
        print(f"Total money: sum(money)")
        # this will print the average money per month
        print(f"Average profit: "sum(money)/len(months))
        #this will find the greatest profit
        print(max(money))
        #this will print the find the greatest lost
        print(min(money))


#Import election CSV and open it 
election_csv = os.path.join("election_data.csv")

with open (election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
#Print the header of the election csv
    cvs_header_election = next(csv_file)
    print(f"Header: "{csv_header_election})
# add assign id, county, and vote to the row in the csv file 
election_id = election_csv[0]
election_County = election_csv[1]
election_vote = election_csv[2]
#add vote for each canadate(their inessales ) to an empty array 
vote_CCS = []
vote_DDG = []
vote_RAD = []
#we start at 0 votes for each canadate 
count = 0 
#we create a loop that counts each vote for the canadates
for vote in election_csv: 
    if vote == 'Charles Casper Stockham':
         vote_CCS = vote + 1
         percent_CCS = vote_CSS / vote
    elif: 
         if vote == "Diana DeGette"
         vote_DDG == vote + 1
         percent_DDG = vote_DDG / vote
    else: 
         vote_RAD = vote + 1
         percent_RAD = vote_RAD /vote
# we print off the results of the election
print(f" Election Results, Total Votes are: sum{vote}")
print(f'Charles Casper Stockman: f{percent_CCS}')
print(f"Diana DeGette: {percent_DDG}")
print(f"Rayman Anthony Foane : {percent_RAD}")
print(f"Winner{max(vote)}")