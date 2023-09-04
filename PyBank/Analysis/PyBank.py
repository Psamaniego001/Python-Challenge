# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:17:07 2023

@author: Saman
"""
import os
import csv

cwd = os.getcwd()
print (cwd)

PyBankdata = "../Resources/budget_data.csv"
months = []
months_adj = []
PnL = []
PnL_Changes = []
PnL_Sum = 0
Changes_Sum = 0

with open (PyBankdata,'r') as file_to_be_read:
    csv_reader = csv.reader(file_to_be_read)
    #skips the headers
    next(file_to_be_read)
    
    for line in csv_reader:
        months.append(line[0])
        PnL.append(line[1])
    #print(len(months))
    
    for x in PnL:
        PnL_Sum += int(x)
    #print(PnL_Sum)
    
    for i in range(len(PnL)-1):
        change = int(PnL[i+1]) - int(PnL[i])
        PnL_Changes.append(change)
    #print(PnL_Changes)
    
    for y in PnL_Changes:
        Changes_Sum += int(y)
    average_changes = Changes_Sum/len(PnL_Changes)
    #print(average_changes)
    
    for z in range(len(months)-1):
        months_adj.append(months[z+1])
    #print(months_adj)

PyBank = list(zip(months_adj,PnL_Changes)) 
#print(PyBank)           

min_number = min(PyBank, key=lambda tup: tup[1])
#print(min_number)
    
max_number = max(PyBank, key=lambda tup: tup[1])
#print(max_number)

with open ("../Main-PyBank.txt",'w') as file_to_be_written:
    file_to_be_written.write("Financial Analysis\n")
    file_to_be_written.write("----------------------------------\n")
    file_to_be_written.write("Total Months: " + str(len(months))+"\n")
    file_to_be_written.write("Total: $" + str(PnL_Sum)+"\n")
    file_to_be_written.write("Average Change: $" +str(round(average_changes,2))+"\n")
    file_to_be_written.write("Greatest Increase in Profits: " + str(max_number)+"\n")
    file_to_be_written.write("Greatest Decrease in Profits: " + str(min_number)+"\n") 
