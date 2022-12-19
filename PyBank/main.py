# import os and csv module
import os
import csv

# lists to store data for use in final metrics
months = []
profit_loss = []
 
# read csv
budget_csv = os.path.join("..", "resources", "budget_data.csv")

with open(budget_csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        # skips first row (header) of csv
        next(csvreader)

        for col in csvreader:

            # loop through csv and find total number of months included
            months.append(col[0])
            print(months)



# loop through csv and find net total of profit/loss

# find changes from one month to the next of P/L and then the avg. 

# find greatest increase from one month to the next (include month/year)

# find greatest decrease from one month to the next (include month/year)

# print results to command line

# export txt file with same results