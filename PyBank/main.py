import os
import csv

# Truncate the decimil
import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number)/stepper

# Declare variables
date = []
profit_loss = []
profit_loss_change = []
net_change = []
increase = []
decrease = []
increase_date = ""
decrease_date = ""

# Read in the file
csvpath = os.path.join(".", "Resources", "budget_data.csv")
# print(pybank_csv)
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    clean_csv = csv.reader(csvfile)
    next(clean_csv, None)

    # Add values
    for row in clean_csv:
        dates = row[0]
        pl = int(row[1])
        date.append(dates)
        profit_loss.append(pl)
        total_months = len(date)
        total_profit = sum(profit_loss)

        # print(clean_csv)
    # Create Analysis Read Out
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}") 
    print(f"Total: $ {total_profit}")

    for i in range(len(profit_loss) - 1):
        profit_loss_change.append(float(profit_loss[i+1]) - float(profit_loss[i]))
        change_sum = sum(profit_loss_change)
        net_change = change_sum / (len(date)-1)

        # Find increase
        increase = max(profit_loss_change)
        increase_date = (date[profit_loss_change.index(max(profit_loss_change))])

        # Find decrease
        decrease = min(profit_loss_change)
        decrease_date = (date[profit_loss_change.index(min(profit_loss_change))])

        # Set additional variables
        average_change = truncate(net_change,2)
        greatest_increase = round(increase)
        greatest_decrease = round(decrease)

    # More Printing
    print(f"Average Change: {truncate(net_change,2)}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# Create the text file
text_file = open("pybank.txt", "w")
text_file.write("Financial Analysis")
text_file.write("\n")
text_file.write("----------------------------")
text_file.write("\n")
text_file.write(f"Total Months: {total_months}")
text_file.write("\n") 
text_file.write(f"Total: $ {total_profit}")
text_file.write("\n")
text_file.write(f"Average Change: {truncate(net_change,2)}")
text_file.write("\n")
text_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
text_file.write("\n")
text_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")