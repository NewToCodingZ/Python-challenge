import os
import csv 
#Import election CSV and open it 
election_csv = os.path.join("election_data.csv")

with open (election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
#Print the header of the election csv
    cvs_header_election = next(csv_file)
   
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
             percent_CCS = vote_CCS / vote
        elif vote == "Diana DeGette":
             vote_DDG == vote + 1
             percent_DDG = vote_DDG / vote
        else: 
             vote_RAD = vote + 1
             percent_RAD = vote_RAD /vote
# we print off the results of the election



output = f'''
Election Results
-------------------------
Total Votes: {vote}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''

print(output)