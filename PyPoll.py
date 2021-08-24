import csv
import os
# import random as rd
# import numpy as np

# print(dir(csv))

# Assign a variable for the file to load the path

#file_to_load = "C:/0_local/BootCamp/3_python/Election_Analysis/Resources/election_results.csv"
#file_to_load = "Resources/election_results.csv"
file_to_load = os.path.join('Resources','election_results.csv')

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    
    # print the header row
    header = next(file_reader)
    print(header)
    # print each row in the csv file
    #for row in file_reader:
    #   print(row[0] + " " + row[-1]) 

# Close the file.
#election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")
#file_to_save = "C:/0_local/BootCamp/3_python/Election_Analysis/analysis/election_analysis.txt"
#file_to_save = "analysis/election_analysis.txt"
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # write some data to the file
    # txt_file.write('Hello World')
    # write three counties to the file
    txt_file.write('Counties in the Election\n')
    txt_file.write('------------------------\n')
    txt_file.write('Arapahoe\n')
    txt_file.write('Denver\n')
    txt_file.write('Jefferson\n')
