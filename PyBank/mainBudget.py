# import the os module
import os

# importing csv module
import csv

# count
count = 0

# Total Revenue = 0
revenue_total = 0

# set path for file
csvpath=os.path.join("budget_data.csv")

# reading csv file
with open(csvpath, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first
    csv_header = next(csvreader)

    # Count the number of rows without the header to calculate the number of months
    row_count = sum(1 for line in open("budget_data.csv"))
    max_gain = 1
    prev_month = 1
    for row in csvreader:
        #print(type(row[1]))
        count += 1
        #revenue=int(row[1])
        #print(revenue)

        this_month = int(row[1])
        revenue_change = int(row[1])
        revenue_total += int(row[1])
        revenue + (float(row[2])
        # change = int(max(this_month,prev_month)) - int(max(this_month,prev_month))
        numList = [ int(this_month) , int(prev_month) ]
        largerNum=max( this_month , prev_month )
        small =  max(this_month,prev_month)
        ) - int(max(this_month,prev_month))
        print (change = max(this_month,prev_month) - max(this_month,prev_month)        prev_month = int(row[1]))
        if revenue_change > max_gain:
            max_gain = revenue_total
            print ('Now revenue_total is:' + str (revenue_total) + "on" + str((row[1]))

print ("Total Months: " + str(count))
print ("Total Revenue: " + str(revenue_total))
# # print ("Greatest Increase in Revenue: " + str(inc_revenue))
# # print ("Greatest Decrease in Revenue: " + str(dec_revenue))
