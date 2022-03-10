#Add our dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign variable to save file
file_to_save = os.path.join("Analysis", "election_analysis")
#Open and read election results file
with open(file_to_load) as election_data:
#To do: Read and analyze the data
#Read the file object with the reader function
    file_reader = csv.reader(election_data)
#Print each row in the CSV file 
    header = next(file_reader)
    print(header)


        

