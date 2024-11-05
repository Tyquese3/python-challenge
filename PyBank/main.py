# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change = []
previous_value = None
net_increase = ["", 0]  # [date, amount]
net_decrease = ["", 999999]  # [date, amount]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # Read header
    header = next(reader)
    
    # Extract first row to avoid appending to net_change
    first_row = next(reader)
    total_months += 1 
    total_net += int(first_row[1])
    previous_value = int(first_row[1])  # Initialize previous_value

    # Process each row of data
    for row in reader:
        current_value = int(row[1])
        total_months += 1  # Increment total months
        total_net += current_value  # Track the total

        # Track the net change
        change = current_value - previous_value
        net_change.append(change)

        # Calculate the greatest increase in profits (month and amount)
        if change > net_increase[1]:
            net_increase[0] = row[0]  # Date
            net_increase[1] = change  # Amount

        # Calculate the greatest decrease in losses (month and amount)
        if change < net_decrease[1]:
            net_decrease[0] = row[0]  # Date
            net_decrease[1] = change  # Amount

        # Update previous_value
        previous_value = current_value

# Calculate the average net change across the months
average_change = sum(net_change) / len(net_change) if net_change else 0

# Generate the output summary
output_summary = ( 
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average Change: ${average_change:,.2f}\n"
f"Greatest Increase in Profits: {net_increase[0]} (${net_increase[1]:})\n"
f"Greatest Decrease in Profits: {net_decrease[0]} (${net_decrease[1]:})\n")

# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)