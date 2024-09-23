# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
net_total = 0
negative_sum = 0
positive_sum = 0
# Add more variables to track other necessary financial data
net_change_list= []
previous_profit_loss = None
greatest_increase = 0
greatest_decrease = float('inf')
greatest_increase_date = ""
greatest_decrease_date = ""


#  Open and read the csv
with open(file_to_load, encoding="UTF-8") as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
       
        # Track the total
        date = row[0] 
        total_months += 1
        profit_loss = int(row[1])
        # Track the net change
        net_total += profit_loss  
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            net_change_list.append(change)  # Store the change
        
          
        # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
        # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date

        previous_profit_loss = profit_loss
# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Print the output
print("Financial Analysis")
print("---------------------------")
report = (
    f'Total number of months: {int(total_months)}\n'
    f'Net Total: ${net_total}\n'
    f'Average Change: ${average_change:.2f}\n'
    f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n'
    f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})'
)
print(report)
# Write the results to a text file
with open(file_to_output, "w", newline='') as txt_file:
    txt_file.write(report)