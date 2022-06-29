# To deliver:
# 1 - total num votes cast
# 2 - complete list of candidates who got votes
# 3 - total num votes for each candidate
# 4 - % votes for each candidate
# 5 - winner based on popular vote


import csv
import os

# variables we'll need with the election results file
total_votes = 0
candidate_options = []
candidate_votes = {}

#build path to and open the election results
file_to_load = os.path.join("resources", "election_results.csv")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Get header row out of data
    headers = next(file_reader)

    for row in file_reader:
        #running tally of votes
        total_votes += 1
        
        #building unique list of candidates
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        #running tally of candidate votes
        candidate_votes[candidate_name] += 1

#build path to and create election analysis txt
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_out:

    #print and export total votes
    election_results = (
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n'
    )

    print(election_results, end = "")
    txt_out.write(election_results)


    #winning candidate variables
    winning_count = 0
    winning_percentage = 0
    winning_candidate = ""


    #loop through output and determine vote totals and winner
    for candidate in candidate_options:
        
        #determine each candidates vote total/percentage
        votes = candidate_votes[candidate]
        candidate_percent = float(votes)/float(total_votes)*100

        #print and export all candidate votes
        candidate_results = (f'{candidate}: {candidate_percent:.1f}% ({votes:,})\n')
        print(candidate_results, end = "")
        txt_out.write(candidate_results)

        #determine the winner
        if (votes > winning_count) and (candidate_percent > winning_percentage):
            winning_count = votes
            winning_percentage = candidate_percent
            winning_candidate = candidate

    #print and export the winner
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n'
    )

    print(winning_candidate_summary)
    txt_out.write(winning_candidate_summary)