#Data we need to retrieve
#1. Total Number of votes cast
#2. complete list of candidates who receieved votes
#3. total number of votes each candidate received 
#4. percentage of votes each candidate won
#5 winner of the election based on popular vote

#import modules
import csv
import os
from typing import NoReturn

#create file name variable
file_to_load=os.path.join("Resources", "election_results.csv")

#initialize variables
total_votes=0
candidate_options=[]
candidate_votes={}
candidate_percentage={}
winning_count=0
winning_percentage=0
winning_candidate=""

#open the file using with sataements
#This file is the election results - use to read data.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    file_reader=csv.reader(election_data)
    
    #print the header row
    headers=next(file_reader)
    #print(headers)

    #Go through each row in the CSV file
    for row in file_reader:
        #increase the vote count for each row
        total_votes+= 1
        #print(row)

        #list of candidates:
        
        current_candidate=row[2]

        if current_candidate not in candidate_options:
            candidate_options.append(current_candidate)
            candidate_votes[current_candidate]=0
        
        candidate_votes[current_candidate]+=1
        #list of votes
        


       
    #print(candidate_votes)
    #print(candidate_options)
    #print(total_votes)
    #print(election_data)

#calculate percentage of votes for each candidate
for vote_candidate, vote_number in candidate_votes.items():

    #calculate and store the vote percentages per candidate
    vote_percentage=float(vote_number)/float(total_votes)*100
    candidate_percentage[vote_candidate]=vote_percentage

    #print each candidate's name, vote count, percent of votes
    print(f"{vote_candidate}: {vote_percentage:.1f}% ({vote_number})\n")

    #determine winning candidate
    if candidate_percentage[vote_candidate]>winning_percentage:
        winning_percentage=candidate_percentage[vote_candidate]
        winning_candidate=vote_candidate
        winning_count=candidate_votes[vote_candidate]






winning_candidate_summary=(
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n")

print(winning_candidate_summary)



#to write to modules:
#1. create a filename variable to a path where the file is to be located
#2. Use the open() function in the "w" mode to open a file and write data to the file

file_to_save=os.path.join("analysis", "election_analysis.txt")

#open the file as a text file
with open(file_to_save, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Total Votes: {total_votes:,}\n")
    outfile.write("---------------------------\n")
    
    #use for loop to display all the candidates, percent, and total votes
    for can in candidate_options:
        outfile.write(f"{can}: {candidate_percentage[can]:.1f}% ({candidate_votes[can]:,})\n")
    
    outfile.write("--------------------------\n")
    outfile.write(f"Winner: {winning_candidate}\n")
    outfile.write(f"Winning Vote Count: {winning_count:,}\n")
    outfile.write(f"Winning Percentage: {winning_percentage:.1f}%\n")
    outfile.write("--------------------------\n")


