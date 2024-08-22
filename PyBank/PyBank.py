
import os
import csv

#Open File path
file_path = r"C:\Bootcamp Class\UCB-VIRT-DATA-PT-07-2024-U-LOLC\Assignments\Module 3\Starter_Code\PyBank\Resources\budget_data.csv"

row_count = 0

textfile_path = r"C:\Bootcamp Class\UCB-VIRT-DATA-PT-07-2024-U-LOLC\Assignments\Module 3\Starter_Code\PyBank\PyBank-Assignment.txt"
with open(textfile_path, 'w') as file:
    file.write("Module 3 - PyBank Assignment Output!\n")

    #Read data in file path
    file.write("Financial Analysis \n")
    file.write("----------------------------------------------------- \n")
    with open(file_path, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        for data in csvreader:
    #The total number of months included in the dataset
            row_count = sum(1 for row in csvreader)
        file.write(f"The total number of months included in the dataset is {row_count}")

    #The net total amount of "Profit/Losses" over the entire period
    with open(file_path, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        profitloss = 0
        next(csvreader)
        
        for row in csvreader:
            profitloss = float(row[1]) + profitloss
        file.write(f"The net total amount of Profit/Losses over the entire period is {profitloss}\n")
        
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    cummulativeplchange = []
    date = []
    with open(file_path, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        currentplrow = next(csvreader)
        currentplvalue = float(currentplrow[1])
    
        for nextplrow in csvreader:
            nextplvalue = float(nextplrow[1])
            pl_change = nextplvalue - currentplvalue
            cummulativeplchange.append(float(pl_change))
            date.append(str(nextplrow[0]))
            currentplvalue = nextplvalue 
            averageplchange = round(sum(cummulativeplchange) / (row_count-1),2)
        #The greatest increase in profits (date and amount) over the entire period
        gincrease = max(cummulativeplchange)
        gincreaseindex = cummulativeplchange.index(gincrease)
        gdecrease = min(cummulativeplchange)
        gdecreaseindex = cummulativeplchange.index(gdecrease)

        file.write(f"The average changes in Profit/Losses over the entire period is {averageplchange} \n")
        
        #The greatest increase in profits (date and amount) over the entire period
        file.write(f"The greatest decrease in profits {date[gincreaseindex]}: {gincrease} \n")
        
        #The greatest decrease in profits (date and amount) over the entire period
        file.write(f"The greatest decrease in profits {date[gdecreaseindex]}: {gdecrease} \n")
