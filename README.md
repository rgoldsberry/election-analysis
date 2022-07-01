# election-analysis
Data Analysis Bootcamp - Module 3

## Project Overview
We were given the task of auditing a recent local congressional election using Python. There were eight main questions to be answered:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout.

## Resources:
- Data Source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code 1.68.1

## Analysis
I worked this project with Python, writing in VSC. The data we received was a csv file with three columns: a ballot id, the county the ballot was cast in, and the candidate the ballot was cast for. We first went through the code and figured out the logic for tallying total votes and the number of votes for each candidate and then applied that same logic to the questions about county turnout. An example of that core of the data gathering is pasted below.
    
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

What we're doing is going row-by-row through the csv file and first, adding that vote to the running tally of total votes. Then we're checking to see if the candidate on the ballot already exists in our list of candidates. If they do not, then we add them to our list and then in either case we add a tally to that specific candidates' vote tally. The same concept was applied to counties with "county_list" and "county_votes" variables.

From that one pass through the csv we had all the data we needed to answer the questions above and from there it was just a question of formatting it to print to the terminal and save it in the [election_reults.txt](analysis/election_results.txt) file.

## Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The three counties that participated are:
  - Jefferson
  - Denver
  - Arapahoe
- The county vote totals were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055) 
  - Arapahoe: 6.7% (24,801)
- The largest county (by votes) in this election was:
  - Denver County, where 82.8% of the ballots were cast, or 306,055 votes.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anythony Doane
- The candidate results were:
  - Charles Casper Stockham: 23.0% (85,213 votes)
  - Diana DeGette: 73.8% (272,892 votes)
  - Raymon Anythony Doane: 3.1% (11,606 votes)
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Future Work
There are a few different options to go from here to expand this code into something more generally useful for the elections department. Two that come to mind that I think we can implement fairly quickly are below.
1. If we wanted to tally up more races at once (like in a bigger election) we could request an additional column in the csv we're delivered that notes what race or initiative that vote is for (so each row looks like: Ballot Id, County, Race, Vote). And then nest all our current logic within another loop that moves through the different races/initiatives.
2. We could "trust-but-verify" that the data we received from the elections team is clean and add in logic to make sure that there are no duplicate ballot ids in the file as we're moving through it.
