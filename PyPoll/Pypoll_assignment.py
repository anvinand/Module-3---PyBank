import os
import csv

#Open File path
file_path = r"C:\Bootcamp Class\UCB-VIRT-DATA-PT-07-2024-U-LOLC\Assignments\Module 3\Starter_Code\PyPoll\Resources\election_data.csv"
#Read data in file path

row_count = 0
def candidatevotes(candidate_names):
    count = 0
    with open(file_path, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for candidate in csvreader:
            if candidate[2] == candidate_names:
                count += 1
        return count
print("Election Results")
print("-----------------------------------------------------")

with open(file_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    #The total number of votes cast  
    for data in csvreader:
        row_count = sum(1 for row in csvreader)
    print("The total number of votes cast", row_count)
print("-----------------------------------------------------")

#A complete list of candidates who received votes
with open(file_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    unique_candidate_names = set()
    next(csvreader)
    for candidate in csvreader:
        unique_candidate_names.add(str(candidate[2]))
    #print(unique_candidate_names)

# Total votes cast for each vote 
c_count = 0
percentage = float
winning_candidate = str
winning_count = 0
for candidate in unique_candidate_names:
    c_count = candidatevotes(candidate)
    percentage = f"{(c_count/row_count):.2%}"
    #print(percentage)
    print(candidate, percentage, c_count)
    if c_count > winning_count:
        winning_count = c_count
        winning_candidate = candidate
print("----------------------------------------------")
print("Winner: ", winning_candidate)
print("----------------------------------------------")

