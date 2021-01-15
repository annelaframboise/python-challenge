import os
import csv

pypoll_csv = os.path.join("Resources", "election_data.csv")

vote_count = 0
unique_candidates = []
votes = []
votes_per_candidate = []
vote_percent = []

with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        vote_count += 1
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
        votes.append(row[2])
    for c in unique_candidates:
        votes_per_candidate.append(votes.count(c))
        vote_percent.append(round(votes.count(c)/vote_count*100,3))

    winner = unique_candidates[votes_per_candidate.index(max(votes_per_candidate))]
       

print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {vote_percent[i]}% {votes_per_candidate[i]}")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

output_path = os.path.join("Analysis","output.txt")

with open(output_path, 'w') as textfile:
    textfile.writelines("Election Results\n")
    textfile.writelines("----------------------------\n")
    textfile.writelines(f"Total Votes: {vote_count}\n")
    textfile.writelines("----------------------------\n")
    for i in range(len(unique_candidates)):
        textfile.writelines(f"{unique_candidates[i]}: {vote_percent[i]}% {votes_per_candidate[i]}\n")
    textfile.writelines("----------------------------\n")
    textfile.writelines(f"Winner: {winner}\n")
    textfile.writelines("----------------------------")
