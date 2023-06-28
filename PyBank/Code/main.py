import os
import csv

# Path to collect data from the Resourcefolder
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

# Define the function

def financial_records(budget_data):
#define the variables
    date_total = str(budget_data[0])
    profit_losses = int(budget_data[1])

# Create the for loops
    total_profit_losses = 0
    for _ in range(profit_losses):
        total_profit_losses = profit_losses + total_profit_losses
        total_profit_losses = total_profit_losses 
    
    change_in_pl = 0
    for _ in range(profit_losses):
        change_in_pl = profit_losses - change_in_pl 
        change_in_pl = change_in_pl 
    percentage_change_in_pl = change_in_pl / 87

    greatest_increase= 0
    for _ in range(profit_losses):
        if profit_losses > profit_losses + 1:
            greatest_increase= profit_losses
    profit_losses = int(budget_data[1])
    greatest_decrease=0
    for _ in range(profit_losses):
        if profit_losses < profit_losses + 1:
            greatest_decrease= profit_losses
    


#print the results
    print(f"Total: {str(total_profit_losses)}")
    print(f"Average change: $ {float(percentage_change_in_pl)}")
    print(f"greatest increase: $ {int(greatest_increase)}")
    print(f"greatest decrease: $ {int(greatest_decrease)}") 
    zipped = zip({str(total_profit_losses)},{float(percentage_change_in_pl)}, {int(greatest_increase)},{int(greatest_decrease)})

# open the csv file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    rowcount = 0
# define the condition and loop and call the function   
    for row in csvreader:
        rowcount+= 1
        financial_records(row)
#print the results
    print("number of months: -", rowcount)
    

output_file_path = os.path.join('..', 'Resources',"results.csv")
zipped = zip(int(rowcount))
with open(output_file_path, 'w') as output_file:
    csvwriter = csv.writer(output_file, delimiter=',')
    csvwriter.writerows(zipped)

   
