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
        print(row)












