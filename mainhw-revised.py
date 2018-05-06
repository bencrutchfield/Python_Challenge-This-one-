import os 
import csv


csvpath = os.path.join('raw_data','budget_data_1.csv')



dates_data = []
revenue_data = []
revenue_delta = []
month = []
revenue = []
average_change_revenue = []
greatest_change_revenue = []


with open(csvpath, newline='') as csvfile: 

    
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        dates_data.append(row[0])
        revenue_data.append(row[1])
        
print(dates_data)
print(revenue_data)

dates_data.pop(0)
revenue_data.pop(0)

for x in range(len(revenue_data)):
    revenue_data[x] = int(revenue_data[x])

total_revenue = sum(revenue_data)
print(total_revenue)
total_months = len(dates_data)
print(total_months) 

for x in range(len(revenue_data)-1):
    change = revenue_data[x+1]-revenue_data[x]
    revenue_delta.append(change)

average_change_revenue = sum(revenue_delta) / len(revenue_delta)

print(average_change_revenue)

greatest_increase_revenue = max(revenue_delta)
greatest_increase_index = revenue_delta.index(greatest_increase_revenue)
best_month = dates_data[greatest_increase_index + 1]
print( best_month,greatest_increase_revenue)


greatest_decrease_revenue = min(revenue_delta)
greatest_decrease_index = revenue_delta.index(greatest_decrease_revenue)
worst_month = dates_data[greatest_decrease_index + 1]
print(worst_month,greatest_decrease_revenue)





output_data = open('analysis.txt','w')
output_data.write("Financial Analysis"+ "\n")
output_data.write("----------------------------"+ "\n")
output_data.write("Total Months: " + str(total_months) + "\n")
output_data.write("Total Revenue: $" + str(total_revenue) + "\n")
output_data.write("Average Revenue Change: $" + str(average_change_revenue) + "\n")
output_data.write("Greatest Increase in Revenue: " + str(best_month) + " ($" + str(greatest_increase_revenue) + ")"+ "\n")
output_data.write("Greatest Decrease in Revenue: " + str(worst_month) + " ($" + str(greatest_decrease_revenue) + ")")

output_data = open('main_results.txt','w')
output_data.write("Financial Analysis"+ "\n")
output_data.write("----------------------------"+ "\n")
output_data.write("Total Months: " + str(total_months) + "\n")
output_data.write("Total Revenue: $" + str(total_revenue) + "\n")
output_data.write("Average Revenue Change: $" + str(average_change_revenue) + "\n")
output_data.write("Greatest Increase in Revenue: " + str(best_month) + " ($" + str(greatest_increase_revenue) + ")"+ "\n")
output_data.write("Greatest Decrease in Revenue: " + str(worst_month) + " ($" + str(greatest_decrease_revenue) + ")") 


output_data.close()



