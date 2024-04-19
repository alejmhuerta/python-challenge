#importing a library/module to read the csv file (a dependacy)
import csv
import os
current_path = os.path.dirname(__file__)
csv_file_path = os.path.join(current_path, "../Resources", "budget_data.csv")

# csv_file_path = "../Resources/budget_data.csv"

with open(csv_file_path) as csvfile:
    reader = csv.reader(csvfile)
    #skipping header 
    next(reader) 

    total_months = 0
    total = 0
    previous_value = None
    changes = []
    greatest_increase = 0
    greatest_decrease = 0
    increase_month = None
    decrease_month = None
    for row in reader:
        total_months = total_months + 1 
        total = total + int(row[1])
        current_value = int(row[1])
        if previous_value != None:
            change = current_value - previous_value
            changes.append(change)

        if previous_value != None and current_value > previous_value:
            increase_sum = current_value - previous_value
            if increase_sum > greatest_increase:
                greatest_increase = increase_sum
                increase_month = row[0]

        if previous_value != None and current_value < previous_value:
            decrease_sum = current_value - previous_value
            if decrease_sum < greatest_decrease:
                greatest_decrease = decrease_sum
                decrease_month = row[0]


        previous_value = current_value

    sum = 0
    for i in range(len(changes)):
        sum = sum + changes[i]
    average = sum/len(changes)

print(f"Total Months: {total_months}")
print(f"Total: ${total}")
# print(f"Average Change: {round(average, 2)}")
print(f"Average Change: {average:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")



       

