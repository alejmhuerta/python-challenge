#importing a library/module to read the csv file (a dependacy)
import csv
# import os
# current_path = os.path.dirname(__file__)
# csv_file_path = os.path.join(current_path, "../Resources", "budget_data.csv")

csv_file_path = "../Resources/budget_data.csv"

with open(csv_file_path) as csvfile:
    reader = csv.reader(csvfile)
    #skipping header 
    next(reader) 

    total_months = 0
    total = 0
    for row in reader:
        total_months = total_months + 1 
        total = total + int(row[1])

print(f"Total Months: {total_months}")
print(f"Total: ${total}")


       

