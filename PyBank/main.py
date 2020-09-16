
# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("output", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
prev_net = 0
greatest_dec_amt = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    start = next(reader)
    start_profit = int(start[1])  
    total_months = total_months + 1  
    total_net = total_net + start_profit
    prev_net = start_profit

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        
        # Track the net change 
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        
        net_change_list.append(net_change)
        #need to keep up with which month goes with which net change for later to need to add this to a list to keep index with n_c
        month_of_change = month_of_change + [row[0]]  # what is this type?(list) why this way over append?
        #could we not just append this and have the same result? try it below
#        month_of_change.append(row[0])
        

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0]
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0]
                    
        
# Calculate the Average Net Change
net_monthly_avg = (sum(net_change_list))/len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print (output)

#Open file using write mode. Specify the variable to hold the contents
with open (file_to_output, 'w') as txtfile:
    txtfile.write(output)
    
 
 
 
 