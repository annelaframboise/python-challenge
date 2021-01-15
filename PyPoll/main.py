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

    # find the winner using index position of the max count in votes_per_candidate
    winner = unique_candidates[votes_per_candidate.index(max(votes_per_candidate))]
       

# unique_candidates_set = set(candidates)
# unique_candidates = list(unique_candidates_set)

#     for i in range(1,len(profit)):
#         profit_change.append(profit[i]-profit[i-1])
#         sum_profit = sum(profit)
#         avg_change = sum(profit_change)/len(profit_change)

# max_avg_change = max(profit_change)
# min_avg_change = min(profit_change)
# max_dates = str(dates[profit_change.index(max_avg_change)+1])
# min_dates = str(dates[profit_change.index(min_avg_change)+1])
# sum_profit = "{:.2f}".format(sum_profit)
# avg_change = "{:.2f}".format(avg_change)
# max_avg_change = "{:.2f}".format(max_avg_change)
# min_avg_change = "{:.2f}".format(min_avg_change)

print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print(f"Candidates: {unique_candidates}")
print("----------------------------")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {vote_percent[i]}% {votes_per_candidate[i]}")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")
# print(f"Total: ${sum_profit}")
# print(f"Average Change: ${avg_change}")
# print(f"Greatest Increase in Profit: {max_dates} ${max_avg_change}")
# print(f"Greatest Decrease in Profit: {min_dates} ${min_avg_change}")

# output_path = os.path.join("output.txt")

# end_list = ["Financial Analysis \n","---------------------------- \n", f"Total Months: {row_num} \n", f"Total: ${sum(profit)} \n",
#     f"Average Change: ${avg_change} \n", f"Greatest Increase in Profit: {max_dates} ${max_avg_change} \n", f"Greatest Decrease in Profit: {min_dates} ${min_avg_change} \n"]

# with open(output_path, 'w') as textfile:
#     textfile.writelines(end_list)