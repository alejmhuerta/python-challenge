import csv
import os
current_path = os.path.dirname(__file__)
csv_file_path = os.path.join(current_path, "../Resources","election_data.csv")

with open(csv_file_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    total_votes = 0
    # candidates = []
    percent_votes = {} 
    for row in reader:
        total_votes = total_votes + 1
        candidate = row[2]

        # if candidate not in candidates:
        #     candidates.append(candidate)

        if candidate not in percent_votes:
            percent_votes[candidate] = 1
        else:
            percent_votes[candidate] = percent_votes[candidate] + 1 
        

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

winner = None

for key, value in percent_votes.items():
    percentage = (value / total_votes) * 100
    print(f"{key}: {percentage:.3f}% ({value})")
    if winner == None:
        winner = key
    elif value > percent_votes[winner]:
        winner = key

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



