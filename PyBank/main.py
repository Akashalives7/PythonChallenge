# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Path to collect data from the csv file
Budget_data = open("budget_data.csv", "r")

# Read the header row first
csv_header= next(csv_header)
print(f"Header:{csv_header}")

    with open(input, "rU") as inf
            incsv = csvreader(inf)
            header = next(incsv, None)
            Revenue = [float(row[Revenue]) for row in incsv]

avg_revenue=sum(Revenue,0.)/(1 and len(Revenue))
max_revenue = max(Revenue)
min_revenue = min(Revenue)
                
