# Election_Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election:

1. Determine total number of votes cast.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county.
3. Determine the county with the largest number of votes.
4. Provide a breakdown of the number of votes and the percentage of total votes for each candidate in the election.
5. Determine the winner of the election based on popular vote.

The Board of Elections has provided voting data in a CSV file detailing each voter's Ballot ID, County, and Candidate Selection. I used Python and imported the built-in module "csv" to pull information from the dataset and perform operations. During the analysis I created variables, lists, and dictionaries to store the election information and used for loops and decision statements to process the stored information. The full set of resources and the election audit results are shown below.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.9, Visual Studio Code, 1.63.2

## Election Audit Results

<img width="348" alt="Screen Shot 2022-01-09 at 5 40 36 PM" src="https://user-images.githubusercontent.com/95327115/148704141-80205943-cfe4-44d6-97f1-eddaf12b721f.png">

The analysis of the election shows:
- There were 269,711 votes cast.
- The county results were:
    - Jefferson County accounted for 10.5% of the vote and 38,855 votes.
    - Denver County accounted for 82.8% of the vote and 306,005 votes.
    - Arapahoe accounted for 6.7% of the vote and 24,801 votes.
- Denver County had the largest number of votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate result were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 23.0% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette with 73.8% of the vote and 272,892 votes.

## Election Audit Summary

In an effort to establish a continued relationship with the Colorado Board of Elections, I designed the election audit Python script 'PyPoll_Challenge.py'  to work with future election. The script may be used, with minor modifications, for any election given a CSV datafile input containing the voting results. With slight modifications, the script will determine the total number of votes, list of participating counties, county voting breakdown, list of all candidates, candidate voting breakdown, and the winner of the election by majority vote.

The script must be modified to read the correct voting data input as shown in lines 8-9 below.

<img width="600" alt="Screen Shot 2022-01-09 at 5 41 18 PM" src="https://user-images.githubusercontent.com/95327115/148704152-9a2adda6-5be8-40d1-a95e-fe33be0374b5.png">

Additionally, the script must be modified to read the correct columns from the CSV file as used in lines 46-50. 

<img width="500" alt="Screen Shot 2022-01-09 at 5 41 42 PM" src="https://user-images.githubusercontent.com/95327115/148704157-53ec5f4c-0b61-4e82-9f62-afc5582bd6cb.png">

Finally, the script can be modified to display the saved results in a text file in any format. If requested, other information could be determined and displayed such as candidate voting results per county.
