# Import operating system

import os

# Import CSV reading Module

import csv

# Define file path

budget = os.path.join('Resources', 'budget_data.csv')


# Solving for part 1  "The total number of months included in the dataset"

# Define Variables

row_count = 0


# Open / Read CSV

with open(budget, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    # skip the first line so it doesn't count the header/row name
   
    next(csv_reader, None)
   
    # Find count of Dates by counting th number of rows in the CSV
   
    for row in csv_reader:
     row_count += 1

    # The total number of months included in the dataset

    print('Total months:' + str(row_count)) 



    
#Solving for part 2 "The net total amount of "Profit/Losses" over the entire period"

# Define variables

net_total = 0.0

# Open / Read CSV

with open(budget, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # skip the first line so it doesn't count the header/row name

    next(csv_reader, None)

    # Iterate throught the second column (Profit/Losses)       

    for row in csv_reader: 
        try:
           # Convert all values to int

            profit_loss = int(row[1])

            # Add all values in second column together
            net_total += profit_loss
       
        except:
           pass
    
    # Print The net total amount of "Profit/Losses" over the entire period

    print('Total:' + "$" + str(net_total))




# Solving for part 3 "The changes in "Profit/Losses" over the entire period, and then the average of those changes"



# Open / Read CSV

with open(budget, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

     # skip the first line so it doesn't count the header/row name

    next(csv_reader, None)

    # Define Variables
    pl = []

    length = []

    change = []

    # Read through variables to fill the list

    for row in csv_reader:
        pl.append(int(row[1]))
        length.append(row[0])
    # Solve for average change
    for i in range(1, len(pl)):
        change.append((int(pl[i]) - int(pl[i-1])))
    
    pl_average = sum(change) / len(change)


    # Print The changes in "Profit/Losses" over the entire period, and then the average of those changes

    print("Average Change:" + "$" + str(round(pl_average)))

   
# Solving for parts 4 and 5 The greatest increase in profits (date and amount) over the entire period /
# and The greatest decrease in profits (date and amount) over the entire period

    # Using the same data captured when finding the average change we can pass the data through the "min" and "max" functions to find the solution

    pl_greatest = max(change)

    pl_min = min(change)

    # Print The greatest increase in profits (date and amount) over the entire period

    print('Greatest Increase in Profits:' + '$' + str(pl_greatest))

    # Print The greatest Decrease in profits (date and amount) over the entire period  

    print('Greatest Decrease in Profits:' + '$' + str(pl_min))


# Output data to a text file

# creats new text file called 'output'

f = open('output.txt', 'w')

# Writing information to the text file and moving to the next line using "\n"

f.write('Financial Analysis' + '\n')

f.write('...............................................................' + '\n')

f.write('Total Months:' + str(row_count) + '\n')

f.write('Total:' + "$" + str(net_total) + '\n')

f.write("Average Change:" + "$" + str(round(pl_average)) + '\n')

f.write('Greatest Increase in Profits:' + '$' + str(pl_greatest) + '\n')

f.write('Greatest Decrease in Profits:' + '$' + str(pl_min))

f.close()







  