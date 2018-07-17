# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Path to collect data from the csv file
Budget_data = open("budget_data.csv", "r")

average = 0.0
total = 0
max = 0.0
min = 0.0

# Read the header row first
csv_header= next(csv_header)
print(f"Header:{csv_header}")

for line in budget

print("Average:", average)
print("MaximumL:", max)
                
