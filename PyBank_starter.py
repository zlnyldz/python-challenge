# -- coding: UTF-8 --
"""PyBank Homework Starter File."""
# Dependencies
import csv
import os
# Set the working directory to ensure it's correct
os.chdir("C:/Users/zilan/DataClass/homework/python-challenge/Starter_Code/PyBank")
print("Changed working directory:", os.getcwd())
# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("budget_analysis.txt")  # Output file path
# Print the file path being used to debug
print("File path being used:", file_to_load)
# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
previous_profit = 0
greatest_increase = ["", 0]  # Month and amount
greatest_decrease = ["", float("inf")]  # Month and amount
try:
    # Open and read the CSV file
    with open(file_to_load, mode='r') as financial_data:
        reader = csv.reader(financial_data)
        # Skip the header row
        header = next(reader)
        # Extract the first row to initialize values properly
        first_row = next(reader)
        total_months += 1
        total_net += int(first_row[1])
        previous_profit = int(first_row[1])
        # Process each row of data
        for row in reader:
            # Update the total number of months and total net amount
            total_months += 1
            total_net += int(row[1])
            # Calculate the net change
            net_change = int(row[1]) - previous_profit
            net_change_list.append(net_change)
            # Check for greatest increase in profits
            if net_change > greatest_increase[1]:
                greatest_increase = [row[0], net_change]
            # Check for greatest decrease in profits
            if net_change < greatest_decrease[1]:
                greatest_decrease = [row[0], net_change]
            # Update previous_profit to the current row's profit value
            previous_profit = int(row[1])
    # Calculate the average net change
    if len(net_change_list) > 0:
        average_change = sum(net_change_list) / len(net_change_list)
    else:
        average_change = 0  # Handle division by zero in case of no data
    # Generate the output summary
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )
    # Print the output to the terminal
    print(output)
    # Write the results to a text file
    with open(file_to_output, mode='w') as txt_file:
        txt_file.write(output)
except FileNotFoundError:
    print(f"Error: The file at {file_to_load} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
