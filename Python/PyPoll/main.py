#Import modules
import os
import csv

#Path to csv
#In the resources folder - renamed file
poll_csv = os.path.join("Resources", "election_data.csv")

#Variables
totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

#Read CSV & clean file
with open(poll_csv) as csvfile:

    #CSV specifies delimiter
    csvReader = csv.reader(csvfile, delimiter = ',')

    #Read header
    csvHeader = next(csvReader)

    #Read each row of data
    for row in csvReader:
        
        #The total number of votes cast
        totalVotes += 1

        #The total number of votes each candidate won
        if (row[2] == "Khan"):
            khanVotes += 1
        elif (row[2] == "Correy"):
            correyVotes += 1
        elif (row[2] == "Li"):
            liVotes += 1
        else: otooleyVotes += 1

#The winner of the election based on popular vote
#max function returns highest value
winner = max(khanVotes, correyVotes, liVotes, otooleyVotes)

if winner == khanVotes:
    winnerName = "Khan"
elif winner == correyVotes:
    winnerName = "Correy"
elif winner == liVotes:
    winnerName = "Li"
else: winnerName = "O'Tooley" #if no one else then otooley

#The percentage of votes each candidate won
khanPercent = khanVotes / totalVotes
correyPercent = correyVotes / totalVotes
liPercent = liVotes / totalVotes
otooleyPercent = otooleyVotes / totalVotes

#Final analysis (A complete list of candidates who received votes)
#.3% gives three decimal points
print(f"Election Results")
print(f"------------------")
print(f"Total votes: {totalVotes}")
print(f"------------------")
print(f"Khan: {khanPercent: .3%} ({khanVotes})")
print(f"Correy: {correyPercent: .3%} ({correyVotes})")
print(f"Li: {liPercent: .3%} ({liVotes})")
print(f"O'Tooley: {otooleyPercent: .3%} ({otooleyVotes})")
print(f"------------------")
print(f"Winner: {winnerName}")
print(f"------------------")

#Text output
output_path = 'Election_Results.txt'
with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow([f"------------------"])
    csvwriter.writerow([f'Total votes: {totalVotes}'])
    csvwriter.writerow([f"------------------"])
    csvwriter.writerow([f"Khan: {khanPercent: .3%} ({khanVotes})"])
    csvwriter.writerow([f"Correy: {correyPercent: .3%} ({correyVotes})"])
    csvwriter.writerow([f"Li: {liPercent: .3%} ({liVotes})"])
    csvwriter.writerow([f"O'Tooley: {otooleyPercent: .3%} ({otooleyVotes})"])
    csvwriter.writerow([f"------------------"])
    csvwriter.writerow([f"Winner: {winnerName}"])
    csvwriter.writerow([f"------------------"])