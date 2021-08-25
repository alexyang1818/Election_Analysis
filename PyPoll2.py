import csv
import os

file_to_load = os.path.join('Resources','election_results.csv')

# 1. Initialize a total vote counter
total_votes = 0

# list of votes for each candidates: list of dict: [{name:'', votes:}, {name:'', votes:}, {name:'', votes:}]
candidate_votes = []

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    
    # print the header row
    header = next(file_reader) # also removes the header row from file_reader for the following analysis
    print(header)
    # print each row in the csv file
    
    # 2. Add to the total vote counter
    for row in file_reader:
        total_votes += 1
        # if total_votes == 1:
        #     print(row)
        # find and save the unique candidate names
        candidate_name = row[2]
        candidate_found = False

        for candidate in candidate_votes:
            if candidate_name == candidate['name']:
                candidate['votes'] += 1
                candidate_found = True
        
        if candidate_found == False:
            candidate_votes.append({'name':candidate_name, 'votes':1})

winning_candidate = ''
winning_votes = 0
winning_percentage = 0

for candidate in candidate_votes:
    candidate['percentage'] = candidate['votes'] / total_votes * 100
    print(f"{candidate['name']} has {candidate['votes']:,} votes, {candidate['percentage']:.1f}% of the total votes.")
    if candidate['votes'] >= winning_votes:
        winning_candidate = candidate['name']
        winning_votes = candidate['votes']
        winning_percentage = candidate['percentage']

winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_votes: ,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"-----------------------------\n"
)

print(winning_candidate_summary)

""" 
        # count votes for each candidates
        candidate_votes[candidate_name] += 1

# 3. Print the total votes
print(f"Number of total votes: {total_votes}.")
# Print the candidate list
print(candidate_options)
# Print candidate votes
print(candidate_votes)

for candidate_name in candidate_options:
    votes = candidate_votes[candidate_name]
    percentage = float(votes) / float(total_votes)
    print(f"{candidate_name} has {percentage * 100: .1f}% of the vote.")

# declare winning candidate, winning count and winning percentage
winning_candidate = ''
winning_vote = 0
winning_percentage = 0

for candidate_name in candidate_options:
    if candidate_votes[candidate_name] > winning_vote:
        winning_candidate = candidate_name
        winning_vote = candidate_votes[candidate_name]
        winning_percentage = winning_vote / total_votes

winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_vote: ,}\n"
    f"Winning Percentage: {winning_percentage * 100: .1f}%\n"
    f"-----------------------------\n"
)

#print(f"The winner is {winning_candidate}. {winning_candidate} won {winning_vote: ,} out of {total_votes: ,} votes.")
print(winning_candidate_summary)

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
    txt_file.write('Jefferson\n') """
