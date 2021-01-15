import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

profit = []
dates = []
profit_change = []
row_num = 0

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        row_num += 1
        dates.append(row[0])
        profit.append(float(row[1]))
    for i in range(1,len(profit)):
        profit_change.append(profit[i]-profit[i-1])
        sum_profit = sum(profit)
        avg_change = sum(profit_change)/len(profit_change)

max_avg_change = max(profit_change)
min_avg_change = min(profit_change)
max_dates = str(dates[profit_change.index(max_avg_change)+1])
min_dates = str(dates[profit_change.index(min_avg_change)+1])
sum_profit = "{:.2f}".format(sum_profit)
avg_change = "{:.2f}".format(avg_change)
max_avg_change = "{:.2f}".format(max_avg_change)
min_avg_change = "{:.2f}".format(min_avg_change)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_num}")
print(f"Total: ${sum_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profit: {max_dates} ${max_avg_change}")
print(f"Greatest Decrease in Profit: {min_dates} ${min_avg_change}")

output_path = os.path.join("Analysis","output.txt")

end_list = ["Financial Analysis \n","---------------------------- \n", f"Total Months: {row_num} \n", f"Total: ${sum(profit)} \n",
    f"Average Change: ${avg_change} \n", f"Greatest Increase in Profit: {max_dates} ${max_avg_change} \n", f"Greatest Decrease in Profit: {min_dates} ${min_avg_change} \n"]

with open(output_path, 'w') as textfile:
    textfile.writelines(end_list)