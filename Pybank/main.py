import os
import csv

#Path to collect data from Resources folder
filepath=os.path.join("Resources", "budget_data.csv") 
file_to_output = os.path.join("Analysis", "pybank_analysis.txt")   
#define variables
month_counter=1
total_revenue=0
increase_profits=0
decrease_losses=0
increase_profits_month=""
decrease_losses_month=""
#Read in the csv file
with open(filepath, "r") as csvfile:

    #Split the data on commas
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    first_row=next(csvreader)
    total_revenue=int(first_row[1])
    previous_month=int(first_row[1])
    first_month=str(first_row[0])
    change_list=[]
    month_list=[first_row[0]]
    

    for row in csvreader:
    
    #total months
        month_counter+= 1
    #net total amount of "profitLosses" over the entire period
        total_revenue=total_revenue+int(row[1])
    #calculate change in current value- previous value
        change=int(row[1])-previous_month
        previous_month=int(row[1])
        change_list.append(change)
        month=row[0]
        month_list.append(month)
    #calculate greatest increase
        if change>increase_profits:
            increase_profits=change
            increase_profits_month=month
        if change<decrease_losses:
           decrease_losses=change
           decrease_losses_month=month
        
        

#average
sum_changes=sum(change_list)
num_changes=len(change_list)
average_change=(sum_changes/num_changes)


output=(
f"Financial Analysis\n"
f"---------------------------------\n"
f"Total Months: {month_counter}\n" 
f"Total: ${total_revenue}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {increase_profits_month} (${increase_profits})\n"
f"Greatest Decrease in Profits: {decrease_losses_month} (${decrease_losses})\n"
)

print(output)
with open(file_to_output, "w")  as outputfile: 
    outputfile.write(output)
