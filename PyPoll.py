#Data we need to retrieve
#1. Total Number of votes cast
#2. complete list of candidates who receieved votes
#3. total number of votes each candidate received 
#4. percentage of votes each candidate won
#5 winner of the election based on popular vote

#import modules
import csv
import os

#create file name variable
file_to_load=os.path.join("Resources", "election_results.csv")

#open the file using with sataements
#This file is the election results - use to read data.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    file_reader=csv.reader(election_data)
    
    #print the header row
    headers=next(file_reader)
    print(headers)

    #Print each rwo in the CSV file
    #for row in file_reader:
     #   print(row)
    #print(election_data)


#to write to modules:
#1. create a filename variable to a path where the file is to be located
#2. Use the open() function in the "w" mode to open a file and write data to the file

file_to_save=os.path.join("analysis", "election_analysis.txt")

#open the file as a text file
with open(file_to_save, "w") as outfile:
    #Title header and format:
    outfile.write("Counties in the Election\n")
    outfile.write("-------------------------\n")
    #Write three counties to the file
    outfile.write("Arapahoe\nDenver\nJefferson")


