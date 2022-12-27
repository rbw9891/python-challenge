# import os, csv, and statistics module
import os
import csv
from statistics import mean 

# lists to store data for use in final metrics
months = []
profit_loss = []
 
# file path
budget_csv = os.path.join("resources", "budget_data.csv")
# open csv with read method
with open(budget_csv, "r") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        # stores header in variable and skips
        header = next(csvreader)

        for col in csvreader:

            # append values of first column (Date) to the months variable
            months.append(col[0])
            # append values of the second column (Profit/Losses) to the profit_loss variable
            profit_loss.append(int(col[1]))
            
# create variable and use len() to find total number of months in data set
num_months = len(months)

# print title
print("Financial Analysis \n")
# print dash break line
print("----------------------------\n")
# print total number of months to the terminal
print(f"Total Months: {num_months}\n")

# create variable and use sum method for finding total P/L
net_profit = sum(profit_loss)
# print total P/L to the terminal
print(f"Total: ${net_profit}\n")

# list comprehension to create new list of differences (changes) from one month to the next
total_changes = [(profit_loss[i+1])-(profit_loss[i]) for i in range(len(profit_loss)-1)]

# print average (using statistics module) of the total changes list rounded to 2 decimal places
print(f"Average Change: ${round((mean(total_changes)),2)}\n")

# print greatest decrease from one month to the next with corresponding month using index of months and max total changes 
print(f"Greatest Increase in Profits: {months[(total_changes.index(max(total_changes)))+1]} (${max(total_changes)})\n")

# print greatest decrease from one month to the next with corresponding month using index of months and min total changes
print(f"Greatest Decrease in Profits: {months[(total_changes.index(min(total_changes)))+1]} (${min(total_changes)})")



# export txt file with same results
output_txt = os.path.join("analysis", "analysis_pybank.txt")

with open(output_txt, "w") as txtfile:

    txtfile.write("Financial Analysis \n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {num_months}\n")
    txtfile.write(f"Total: ${net_profit}\n")
    txtfile.write(f"Average Change: ${round((mean(total_changes)),2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {months[(total_changes.index(max(total_changes)))+1]} (${max(total_changes)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {months[(total_changes.index(min(total_changes)))+1]} (${min(total_changes)})")

    
