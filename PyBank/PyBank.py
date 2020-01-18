#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
bank_file = "desktop/school/gt-data/homework/03-python/instructions/PyBank/Resources/budget_data.csv"
bank_file_read = pd.read_csv(bank_file)
bank_file_read.head(10)


# In[56]:


import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(bank_file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")


# In[63]:


#Exporing to .txt file
#output = open("output.txt", "w")

file = open("output.txt","w")

file.write("Financial Analysis")
file.write("---------------------")
file.write(f"Total: ${str(total_pl)}")
file.write(f"Average Change: ${str(round(avg_change,2))}")
file.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
file.write(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
#file.write()
#file.write()
#line2 = "---------------------"
#line3 = str(f"Total Months: {str(total_months)}")
#line4 = str(f"Total: ${str(total_pl)}")
#line5 = str(f"Average Change: ${str(round(avg_change,2))}")
#line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
#line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
#output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

file.close()

