# import os, csv, and statistics module
import os
import csv
from statistics import mean 

votes = []
candidates = []
stockham = []
degette = []
doane = []

# read csv
election_csv = os.path.join("resources", "election_data.csv")

with open(election_csv, "r") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        #vote_dict = {col: for col in csvreader}

        # store header in variable
        header = next(csvreader)

        for col in csvreader:

            # append the values of the first column to votes list
            votes.append(col[0])

            # append values of the third column (Candidates) to the candidate list
            candidates.append(col[2])

num_voters = len(votes)

print(num_voters)

stockham = [x for x in candidates if x == "Charles Casper Stockham"]
stockham_ct = len(stockham)
print(stockham_ct)

degette = [x for x in candidates if x == "Diana DeGette"]
degette_ct = len(degette)
print(degette_ct)

doane = [x for x in candidates if x == "Raymon Anthony Doane"]
doane_ct = len(doane)
print(doane_ct)

perc_stockham = round((stockham_ct/num_voters)*100, 3)

print(perc_stockham)

perc_degette = round((degette_ct/num_voters)*100, 3)

print(perc_degette)

perc_doane = round((doane_ct/num_voters)*100, 3)

print(perc_doane)

results = [stockham_ct,degette_ct,]

# find len of voter list created from csv read

# find unique values in candidate list and print them once

# find percentage of votes each candidate received

# find total number of votes for each candidate

# print winner 

# all on terminal

# export to txt file