import os
import csv


candidates = []
num_votes = 0
vote_counts = []


filepath = os.path.join('election_data.csv')


with open(filepath,newline="") as csvfile:
   csvreader = csv.reader(csvfile)

   row = next(csvreader,None)
   for row in csvreader:

       num_votes = num_votes + 1
       candidate = row[2]

       if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_counts[candidate_index] = vote_counts[candidate_index] + 1
       else:
           candidates.append(candidate)
           vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
for count in range(len(candidates)):
   vote_percentage = round((vote_counts[count]/num_votes*100),3)
   percentages.append(vote_percentage)
   if vote_counts[count] > max_votes:
       max_votes = vote_counts[count]
       print(max_votes)
       max_index = count
winner = candidates[max_index]


print("Election Results")
print("--------------------------")
print("Total Votes: " + str(num_votes))
print("--------------------------")
for count in range(len(candidates)):
   print(str(candidates[count]) + ": " + str(percentages[count]) + "% (" + str(vote_counts[count]) + ")")
print("---------------------------")
print("Winner: (" + str(winner) + ")" )
print("---------------------------")

output_dest = os.path.join('pypoll_results.txt')
with open(output_dest, 'w') as writefile:
    writefile.write("Election Results\n")
    writefile.write("--------------------------\n")
    writefile.write("Total Votes: " + str(num_votes)+ "\n")
    writefile.write("--------------------------\n")
    for count in range(len(candidates)): writefile.write(str(candidates[count]) + ": " + str(percentages[count]) + "% (" + str(vote_counts[count]) + ")\n")
    writefile.write("---------------------------\n")
    writefile.write("Winner: (" + str(winner) + ")\n" )
    writefile.write("---------------------------\n")