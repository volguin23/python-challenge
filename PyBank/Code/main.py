import os
import csv

# Reference the CSV file and folder
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")
# Create the variables and a couplee of lists to save both columns from the data set
months = []
pl = []
total_months = 0
total_pl = 0
acummulation_pl= 0
change = 0


#Opening the CSV file and delimiting by commas
with open(budget_data_csv, newline = "") as csvfile:
    csv_file = csv.reader(csvfile, delimiter = ",")

    # Read the header row
    csv_header = next(csv_file)

    # create variables to avoid using the first rows
    header = next(csv_file)
    total_months += 1
    total_pl += int(header[1])
    acummulation_pl = int(header[1])
    
    #Create a for to iterate through the data of the csv file
    for row in csv_file:
        months.append(row[0])
        change = int(row[1])-acummulation_pl
        pl.append(change)
        acummulation_pl = int(row[1])
        #Formula to obtain the total months
        total_months += 1
        #Formula to get the total of the second row: profit/losses
        total_pl = total_pl + int(row[1])

    #Formula to get the greatest increase, outside the for and creating an index to keep account of the changes
    increase = max(pl)
    increase_in = pl.index(increase)
    month_increase = months[increase_in]
    #Formula to get the greatest decrease, outside the for and creating an index to keep account of the changes
    decrease = min(pl)
    decrease_in = pl.index(decrease)
    month_decrease = months[decrease_in]
    #Get the average change in the PL Column by dividing by the len of the list.
    average_change = sum(pl)/len(pl)
    
#Displaying information
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {month_increase} (${str(increase)})")
print(f"Greatest Decrease in Profits: {month_decrease} (${str(decrease)})")

#Create the txt file with the results
results = open("results.txt", "w")
# Create the lines and print them in the results txt file creating tupples with the results
l1 = str(f"Total Months: {str(total_months)}")
l2 = str(f"Total: ${str(total_pl)}")
l3 = str(f"Average Change: ${str(round(average_change,2))}")
l4 = str(f"Greatest Increase in Profits: {month_increase} (${str(increase)})")
l5 = str(f"Greatest Decrease in Profits: {month_decrease} (${str(decrease)})")
results.write('{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5))