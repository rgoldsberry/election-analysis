# To deliver:
# 1 - total num votes cast
# 2 - complete list of candidates who got votes
# 3 - total num votes for each candidate
# 4 - % votes for each candidate
# 5 - winner based on popular vote


import csv
import os

#build path to and open the election results
file_to_load = os.path.join("resources", "election_results.csv")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)



#build path to and create election analysis txt
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_out:
    txt_out.write("Counties in the Election\n")
    txt_out.write("-------------------------\n")
    txt_out.write("Arapahoe\n")
    txt_out.write("Denver\n")
    txt_out.write("Jefferson")