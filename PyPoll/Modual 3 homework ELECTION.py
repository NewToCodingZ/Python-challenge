import os
import csv 
dirname = os.path.dirname(__file__)
#Import election CSV and open it 
election_csv = os.path.join(dirname,"Resources","election_data.csv")
print(election_csv)

with open (election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
#Print the header of the election csv
    cvs_header_election = next(csvreader)
   
# add assign the row in the csv file 


#add vote for each canadate(their inessales ) to an empty array 
    vote_CCS = 0
    vote_DDG = 0
    vote_RAD = 0
#we start at 0 votes for each canadate 
    count = 0 

#we create a loop that counts each vote for the canadates
    for row in csvreader: 
        if row[2] == 'Charles Casper Stockham':
             vote_CCS += 1
 #            percent_CCS = vote_CCS / vote
        elif row[2] == "Diana DeGette":
             vote_DDG += 1
  #           percent_DDG = vote_DDG / vote
        else: 
             vote_RAD += 1
  #           percent_RAD = vote_RAD /vote

  #winner = vote.max()
# we print off the results of the election

total_vote = vote_CCS+ vote_DDG + vote_RAD
winner = ''
if vote_CCS > vote_DDG and vote_CCS > vote_RAD:
     winner = 'Charles'
elif vote_DDG > vote_CCS and vote_DDG > vote_RAD:
     winner = 'Diana DeGette'
else: winner = 'Rad'


output = f'''
Election Results
-------------------------
Total Votes: {total_vote}
-------------------------
Charles Casper Stockham:  {((vote_CCS/total_vote) * 100):.3f}% {vote_CCS}
Diana DeGette: {((vote_DDG/total_vote) * 100):.3f}% {vote_DDG}
Raymon Anthony Doane: {((vote_RAD/total_vote) * 100):.3f}% {vote_RAD}
-------------------------
Winner: {winner}
-------------------------
'''

print(output)