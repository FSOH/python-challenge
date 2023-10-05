

# Importing modules
import os
import csv
# Set relative path for csv file
file_path = './resources/election_data.csv'
candidates = [] # names of candidates list
c_votes = []# number of votes by candidate list
per_votes = []#percentage of total votes by candidates list
total_votes = 0 # total number of votes count

    # Read csv file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Reading header to skip it
    csv_header = next(csvreader)

    for row in csvreader:
       
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            c_votes.append(1)
        else:
            index = candidates.index(row[2])
            c_votes[index] += 1

    # Percentage of votes of each candidate WON
    for votes in c_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        per_votes.append(percentage)

    # he winner of the election based on popular vote
    winner = max(c_votes)
    index = c_votes.index(winner)
    winning_candidate = candidates[index]

# print results
print("Election Results")
print("-"*10)
print(f"Total Votes: {str(total_votes)}")
print("-"*10)
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(per_votes[i])} ({str(c_votes[i])})")
print("-"*10)
print(f"Winner: {winning_candidate}")
print("-"*10)

# Exporting to text file


results_file = os.path.join('analysis', 'PyPoll_results.txt')

PyPolloutput = open(results_file, "w")

line1 = "Election Results"
line2 = "-"*10
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = ("-")*10
PyPolloutput.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(
        f"{candidates[i]}: {str(per_votes[i])} ({str(c_votes[i])})")
    PyPolloutput.write('{}\n'.format(line))
line5 = "-"*10
line6 = str(f"Winner: {winning_candidate}")
line7 = "-"*10
PyPolloutput.write('{}\n{}\n{}\n'.format(line5, line6, line7))




    
