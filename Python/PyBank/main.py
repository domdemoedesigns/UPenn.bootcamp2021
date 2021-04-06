#Import modules
import os
import csv

#Path to csv
#In the resources folder - renamed file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Variables
totalMonths = 0
netTotal = 0
monthlyChange = []
monthlyCount = []
greatestIncrease = 0
greatestMonthlyIncrease = 0
greatestDecrease = 0
greatestMonthlyDecrease = 0

#Read CSV & clean file
with open(budget_csv) as csvfile:

    #CSV specifies delimiter
    csvReader = csv.reader(csvfile, delimiter = ',')

    #Read header & row
    csvHeader = next(csvReader)
    row = next(csvReader)

    #Calculate total months, net total amount of profits/losses & set variables
    #have to initialize outside of for loop
    lastRow = int(row[1]) #using brackets for list
    totalMonths += 1
    netTotal += int(row[1])
    greatestIncrease = int(row[1])
    greatestMonthlyIncrease = row[0]

    #Read each row of data
    for row in csvReader:

        #The total number of months included in the dataset
        totalMonths += 1

        #The net total amount of "Profit/Losses" over the entire period
        netTotal += int(row[1])

        #Calculate the changes in "Profit/Losses" over the entire period
        revenueChange = int(row[1]) - lastRow
        monthlyChange.append(revenueChange)
        lastRow = int(row[1])
        monthlyCount.append(row[0])

        #Average of those changes, date
        averageChange = sum(monthlyChange)/ len(monthlyChange)

        #The greatest increase in profits over the entire period
        if int(row[1]) > greatestIncrease:
            greatestIncrease = int(row[1])
            greatestMonthlyIncrease = row[0]

        highestChange = max(monthlyChange)
        
        #The greatest decrease in losses over the entire period
        if int(row[1]) < greatestDecrease:
            greatestDecrease = int(row[1])
            greatestMonthlyDecrease = row[0]
        
        lowestChange = min(monthlyChange)

#Final analysis
print(f"Financial Analysis")
print(f"--------------------")
print(f"Total months: {totalMonths}")
print(f"Total: ${netTotal}")
print(f"Average change: ${averageChange:.2f}")
print(f"Greatest increase in profits: {greatestMonthlyIncrease}: (${highestChange})")
print(f"Greatest decrease in profits: {greatestMonthlyDecrease}: (${lowestChange})")

#Text output
output_path = "Financial_Analysis.txt"
with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow([f"Financial Analysis"])
    csvwriter.writerow([f"--------------------"])
    csvwriter.writerow([f'Total months: {totalMonths}'])
    csvwriter.writerow([f'Total: ${netTotal}'])
    csvwriter.writerow([f'Average change: ${averageChange:.2f}'])
    csvwriter.writerow([f'Greatest increase in profits: {greatestMonthlyIncrease}: (${highestChange})'])
    csvwriter.writerow([f'Greatest decrease in profits: {greatestMonthlyDecrease}: (${lowestChange})'])