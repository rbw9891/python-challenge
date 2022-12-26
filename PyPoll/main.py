# import os, csv, and statistics module
import os
import csv
from statistics import mean 

# empty list to put ballot id numbers in from csv read
votes = []
# empty list to put candidate choice in from csv read
candidates = []
# empty list to put all votes for Charles Casper Stockham inside of
stockham = []
# empty list to put all votes for Diana DeGette inside of
degette = []
# empty list to put all votes for Raymon Anthony Doane inside of
doane = []

# file path
election_csv = os.path.join("resources", "election_data.csv")
# open csv with read method
with open(election_csv, "r") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        
        # store header in variable and skip line for csv read
        header = next(csvreader)

        for col in csvreader:

            # append the values of the first column (Ballot ID) to votes list
            votes.append(col[0])

            # append values of the third column (Candidates) to the candidate list
            candidates.append(col[2])

# find the length of the votes list where each Ballot ID is unique and len will give us the Total Votes cast
num_voters = len(votes)



# list comprehension to create a list of all of the Stockham votes
stockham = [x for x in candidates if x == "Charles Casper Stockham"]
# create variable to count the length of the stockham list which will equal the amount of votes for said candidate
stockham_ct = len(stockham)
# create variable to find the percentage of votes for stockham, rounded to 3 decimal places
perc_stockham = round((stockham_ct/num_voters)*100, 3)



# list comprehension to create a list of all of the DeGette votes
degette = [x for x in candidates if x == "Diana DeGette"]
# create variable to count the length of the degette list which will equal the amount of votes for said candidate
degette_ct = len(degette)
# create variable to find the percentage of votes for degette, rounded to 3 decimal places
perc_degette = round((degette_ct/num_voters)*100, 3)



# list comprehension to create a list of all of the Doane votes
doane = [x for x in candidates if x == "Raymon Anthony Doane"]
# create variable to count the length of the Doane list which will equal the amount of votes for said candidate
doane_ct = len(doane)
# create variable to find the percentage of votes for Doane, rounded to 3 decimal places
perc_doane = round((doane_ct/num_voters)*100, 3)



# print title
print("Election Results\n")
# print dash line
print("----------------------------\n")
# print Total Votes to the terminal
print(f"Total Votes: {num_voters}\n")
# print dash line
print("----------------------------\n")
# print votes for and percentage votes for Stockham to the terminal
print(f"Charles Casper Stockham: {perc_stockham}% ({stockham_ct})\n")
# print votes for and percentage votes for DeGette to the terminal
print(f"Diana DeGette: {perc_degette}% ({degette_ct})\n")
# print votes for and percentage votes for Doane to the terminal
print(f"Raymon Anthony Doane: {perc_doane}% ({doane_ct})\n")
# print dash line
print("----------------------------\n")
# print the winner Diana DeGette
print("Winner: Diana DeGette\n")
print("----------------------------\n")


# export txt file with same results
output_txt = os.path.join("analysis", "analysis_pypoll.txt")

with open(output_txt, "w") as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Votes: {num_voters}\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {perc_stockham}% ({stockham_ct})\n")
    txtfile.write(f"Diana DeGette: {perc_degette}% ({degette_ct})\n")
    txtfile.write(f"Raymon Anthony Doane: {perc_doane}% ({doane_ct})\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Winner: Diana DeGette\n")
    txtfile.write("----------------------------\n")