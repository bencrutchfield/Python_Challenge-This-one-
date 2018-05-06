
import os


import csv


csvpath = os.path.join('raw_data','budget_data_1.csv')


dates_data = []
revenue_data = []
revenue_delta = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

   
    for row in csvreader:
        dates_data.append(row[0])
        revenue_data.append(row[1])   


dates_data.pop(0)
revenue_data.pop(0)


for i in range(len(revenue_data)):
    revenue_data[i]=int(revenue_data[i])


total_months =len(dates_data)


total_revenue = sum(revenue_data)


for i in range(len(revenue_data)-1):
    change = revenue_data[i+1]-revenue_data[i]
    revenue_delta.append(change)

average_revenue_change = sum(revenue_delta)/len(revenue_delta)


greatest_increase = max(revenue_delta)
greatest_increase_index = revenue_delta.index(greatest_increase)
best_month = dates_data[greatest_increase_index + 1]


greatest_decrease = min(revenue_delta)
greatest_decrease_index = revenue_delta.index(greatest_decrease)
worst_month = dates_data[greatest_decrease_index + 1]


print("Financial Analysis")
print("----------------------------")
print("Total Months: ",total_months)
print("Total Revenue: $",total_revenue)
print("Average Revenue Change: $",average_revenue_change)
print("Greatest Increase in Revenue: ",str(best_month) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Revenue: ",str(best_month) + " ($" + str(greatest_decrease) + ")")


output_file = open('revenue_results.txt','w')
output_file.write("Financial Analysis"+ "\n")
output_file.write("----------------------------"+ "\n")
output_file.write("Total Months: " + str(total_months) + "\n")
output_file.write("Total Revenue: $" + str(total_revenue) + "\n")
output_file.write("Average Revenue Change: $" + str(average_revenue_change) + "\n")
output_file.write("Greatest Increase in Revenue: " + str(best_month) + " ($" + str(greatest_increase) + ")"+ "\n")
output_file.write("Greatest Decrease in Revenue: " + str(worst_month) + " ($" + str(greatest_decrease) + ")")

output_file.close()