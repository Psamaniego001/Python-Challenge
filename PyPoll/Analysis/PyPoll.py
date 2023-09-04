# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 10:36:26 2023

@author: Saman
"""
import os
import csv

cwd = os.getcwd()
print(cwd)

Candidate = []
Unique_candidate = []
Number_of_votes = [0,0,0]
Percent_of_votes = []

PyPolldata = "../Resources/election_data.csv"

with open (PyPolldata,'r') as file_to_be_read:
    csv_reader = csv.reader(file_to_be_read)
    
    next(csv_reader)
    
    for line in csv_reader:
        Candidate.append(line[2])
    number_of_votes = len(Candidate)
    #print(number_of_votes)
    
    for item in Candidate:
        if item not in Unique_candidate:
            Unique_candidate.append(item)
    
    for x in Candidate:
        
        if x in Unique_candidate[0]:
            Number_of_votes[0] += 1
        if x in Unique_candidate[1]:
            Number_of_votes[1] += 1
        if x in Unique_candidate[2]:
            Number_of_votes[2] += 1
        
    #print(Unique_candidate)
    #print(Number_of_votes)
    
    #stores the percentages of the votes and formats the decimals to percentages
    for y in range(len(Number_of_votes)):
        percentage = Number_of_votes[y]/number_of_votes
        Percent_of_votes.append("{:.3%}".format(float(round(percentage,5))))
    
    #print(Percent_of_votes)
    
PyPoll = list(zip(Unique_candidate,Percent_of_votes,Number_of_votes))
#print(PyPoll)


with open ("../Main-PyPoll.txt",'w') as file_to_be_written:
    file_to_be_written.write("Election Results\n")
    file_to_be_written.write("----------------------------------\n")
    file_to_be_written.write(f'Total Votes: {number_of_votes}\n')
    file_to_be_written.write("----------------------------------\n")
    for z in range(len(Number_of_votes)):
        file_to_be_written.write(f'{Unique_candidate[z]}: {Percent_of_votes[z]}, {Number_of_votes[z]}\n')
    file_to_be_written.write("----------------------------------\n")
    max_number = max(Number_of_votes)
    index = Number_of_votes.index(max_number)
    file_to_be_written.write(f'Winner: {Unique_candidate[index]}\n')
    file_to_be_written.write("----------------------------------\n")
   
    
    
    
    
    
    
    
    
    
    
    
    