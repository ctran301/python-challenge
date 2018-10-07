#Modules
import os
import csv

# Set path for file
budget_csv = os.path.join('Resources', 'budget_data.csv')

prof_loss = 0
totalMonths = 0
last = 0
current = 0
difference = 0
monthly_chg = 0
max_change = 0
min_change = 0
max_date = str
min_date = str


#Open and read csv
with open(budget_csv, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

   next(csvreader)
   
   #Read through each row after header
   for row in csvreader:

        totalMonths = totalMonths + 1
        prof_loss = int(row[1]) + prof_loss

    #Loop through columns to find difference between months and total differences
        if (totalMonths-1) == 0:
            current = int(row[1])
        else:
            last = current
            current = int(row[1])

            difference = (((current)-(last)) + difference)

        #counter for how many times you take the difference between months
            monthly_chg = monthly_chg + 1

            #find max and min
            if max_change < (current-last):
                max_change = (current-last)
                max_date= str(row[0])
            else:
                max_change = max_change
            if min_change > (current-last):
                min_change = (current-last)
                min_date= str(row[0])
            else:
                min_change = min_change

        
            

            

    #Find average of the diffencees to find the avg change over each period
avg_change = round (difference/monthly_chg, 2)
            


#Print results

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(prof_loss)}")
print(f"Average Change: ${str(avg_change)}")
print(f"Greatest Increase in Profits: " + " " + max_date + " "+ str(max_change))
print(f"Greatest Decrease in Profits: " + " " + min_date + " "+ str(min_change)) 

output_dest = os.path.join('pybank_results.txt')
with open(output_dest, 'w') as writefile:
    writefile.write("Financial Analysis\n")
    writefile.write("----------------------------\n")
    writefile.write("Total Months: " + str(totalMonths)+"\n")
    writefile.write("Total: $"+str(prof_loss) +"\n")
    writefile.write("Average  Change: $"+str(avg_change)+"\n")
    writefile.write("Greatest Increase in Profits: " + max_date + " (" +str(max_change) + ")"+"\n")
    writefile.write("Greatest Decrease in Profits: " + min_date + " (" +str(min_change) + ")"+"\n")