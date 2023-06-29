import os
import csv

# Path to collect data from the Resourcefolder
election_data_csv = os.path.join("..", "Resources", "election_data.csv")


# Create lists to store the columns
candidates = []
votes= []
percentages = []
votes_total = 0
# open the csv file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)

# define the condition and loop   
    for row in csvreader:
        votes_total+= 1

# create loop to sum the different candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_in = candidates.index(row[2])
            votes.append(1)
        else:
            candidates_in = candidates.index(row[2])
            votes[candidates_in] += 1
#create another loop to get the percentages
    for total_votes in votes:
        votes_percent = (total_votes/votes_total) * 100
        percentages.append(votes_percent)

# formula to find the winner
    winner_candidate = max(votes)
    candidates_in = votes.index(winner_candidate)
    candidate_winner = candidates[candidates_in]

#print the results
print("Results")
print("-------------------")
print(f"Total Votes: {str(votes_total)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentages[i])} ({str(votes[i])})")
print(f"Winner: {candidate_winner}")

#Create the txt file with the results
results = open("results.txt", "w")
# Create the lines and print them in the results txt file creating tupples with the results
l1 = str(f"Results")
l2 = str(f"-----------------")
l3 = str(f"Total Votes: {str(votes_total)}")
results.write('{}\n{}\n{}\n'.format(l1,l2,l3))
for i in range(len(candidates)):
    l6=str(f"{candidates[i]}: {str(percentages[i])} ({str(votes[i])})")
    results.write('{}\n'.format(l6))
l4 = str(f"winner: {candidate_winner}")
results.write('{}\n'.format(l4))