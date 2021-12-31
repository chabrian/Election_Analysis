#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Example of Dependency

#Import the datetime class from the datetime module
#import datetime as dt
#use the now() attribute on the datetime class to get the present time
#now = dt.datetime.now()
#print("The time right now is ", now)
#Packages can also be imported using import
#Modules are usually files with .py extension
#use dir() function to return all functions available on a variable

import csv
import os

#Direct
#assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'

#Indirect
file_to_load = os.path.join("Resources","election_results.csv")

#Write to a file
file_to_save = os.path.join("analysis","election_analysis.txt")
# with open(file_to_save,"w") as txt_file:

#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#initialize total vote counter
total_votes = 0

#initialize a list for candidate options
candidate_options = []

#initialize a dictionary for candidate total votes
candidate_votes = {}

#initialize winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Method1
#open file
#election_data = open(file_to_load, 'r')
#To Do: analysis
#close the file.
#election_data.close()

#Method2
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV file
    for row in file_reader:

        #add to the total vote count
        total_votes += 1

        #get candidates name from each row
        candidate_name = row[2]

        #add candidate name to the options list if not already in options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking vote count / initialize key for new unique candidate
            candidate_votes[candidate_name] = 0

        #add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

#save results to the text file
with open(file_to_save, "w") as txt_file:

    #print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results, end="")
    #save final vote count to text file
    txt_file.write(election_results)

    #determine percentage of votes for each candidate
    for candidate_name in candidate_votes:
        #retrieve vote count for candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100
        #print candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #save candidate results to text file
        txt_file.write(candidate_results)

        #determine the winner
        #First determine if votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            #set winner to the candidates name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)
    #save winning candidate name to text file
    txt_file.write(winning_candidate_summary)














