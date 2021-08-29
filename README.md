# Election_Analysis
## Overview of Election Audit

The purpose of this election analysis audit is to determine the winner candidate and summarize the voting statistics.

## Election Audit Results


The election analysis is displayed as following: 

![Election Results](/analysis/election_results.PNG)

### **Total Votes**
There are 369,711 votes in total.

### **Voting Statistics by County**
Votes are collected from three counties. The Jefferson county has 38,855 votes, which is 10.5% of the total votes. Denver has 306,055 votes (82.8%). Arapahoe has 24,801 votes (6.7%). Therefore, the county with the largest turnout is Denver.

### **Voting Statistics by Candidates**
Three candidates participated this election. Charles Casper Stockham won 85,213 votes, which is 23.0% of the total votes. Diana DeGette won 272,892 votes (73.8%). Raymon Anthony Doane won 11,606 votes (3.1%). Therefore, the winner is Diana DeGette.

## Election Audit Summary

The Python script used here can be modified to analyze any other elections. For example, when multiple winners are expected, the variables of the winner can be replaced with a list. The list then can be sorted to find multiple winners.

```
### testing candidate sorting ###
candidates_sorted = []
sort_index = 0

for candidate_name in candidate_options:
    candidates_sorted.append({"name":candidate_name, "votes":candidate_votes[candidate_name]})

print(candidates_sorted)

for j in range(len(candidates_sorted)-1):
    for i in range(len(candidates_sorted)-1):
        if candidates_sorted[i]["votes"] < candidates_sorted[i+1]["votes"]:
            temp = candidates_sorted[i+1]
            candidates_sorted[i+1] = candidates_sorted[i]
            candidates_sorted[i] = temp

print(candidates_sorted)
```
The above script sorts the candidates in the descending order of their votes. The following output was printed: 
```
[{'name': 'Charles Casper Stockham', 'votes': 85213}, {'name': 'Diana DeGette', 'votes': 272892}, {'name': 'Raymon Anthony Doane', 'votes': 11606}]
[{'name': 'Diana DeGette', 'votes': 272892}, {'name': 'Charles Casper Stockham', 'votes': 85213}, {'name': 'Raymon Anthony Doane', 'votes': 11606}]
```
Another example is to investigate the Ballot IDs to make sure to remove duplicates. 
```
### testing finding duplicate ballots ###
number_of_duplicates = 0
ballot = {}                 # store single ballots
ballots = []                # collect all ballots
ballotIDs = []              # list of ballot ID
ballots_duplicates = []     # record ballots with duplicates

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        ballot = {}
        for i in range(len(header)):
            ballot[header[i]] = row[i]
        ballots.append(ballot)
        ballotIDs.append(ballot[header[0]])

ballotIDs.sort()

for i in range(len(ballotIDs)-1):
    if ballotIDs[i] == ballotIDs[i+1]:
        number_of_duplicates += 1
        ballots_duplicates.append(ballotIDs[i])

print(f"Number of Duplicate Ballots: {number_of_duplicates}")
if number_of_duplicates > 0:
    print(
        f"Duplicated Ballot IDs:\n"
        f"{ballots_duplicates}"
        )
```
Output with original data:
```
Number of Duplicate Ballots: 0
```
Outputs after introducing two duplicates:
```
Number of Duplicate Ballots: 2
Duplicated Ballot IDs:
['1040408', '1833621']
```
