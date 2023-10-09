# Import operating system

import os

# Import CSV reading Module

import csv

# Define CSV filepath

election = os.path.join('Resources/election_data.csv')

# Open / Read CSV

with open(election, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # skip the first line so it doesn't count the header/row name

    next(csv_reader, None)

    # Solving for Part 1 Find "The Total number of Votes Cast"

    # Define Variable
    total_vote = 0

    for row in csv_reader:
     total_vote += 1

    # Print Solution
    print('Total Votes: ' + str(total_vote))

# Solving for Parts 2 , 3 , and 4 (Complete list of candidate, Percentage of vote for each, and the total number of votes for each)

# Open / Read CSV

with open(election, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # skip the first line so it doesn't count the header/row name

    next(csv_reader, None)

    # Define Variables
    total_count_C = 0
    total_count_D = 0
    total_count_R = 0
    Candidate_C =  ('Charles Casper Stockham')
    Candidate_D = ('Diana DeGette')
    Candidate_R =  ('Raymon Anthony Doane')
    
   # Solve for List of candidates and total number of votes
    
    for row in csv_reader:
        if row[2] == Candidate_C:
            total_count_C += 1
        elif row[2] == Candidate_D:
            total_count_D += 1
        elif row[2] == Candidate_R:
            total_count_R += 1

    # Solve for Percentage of Vote

    # Define Variables / function to calculate percentage of votes
    percent_vote_C = total_count_C / total_vote * 100
    percent_vote_D = total_count_D / total_vote * 100
    percent_vote_R = total_count_R / total_vote * 100


# Print the total counts for each candidate
print(f'{Candidate_C}: {percent_vote_C:.3f}% ({total_count_C})')
print(f'{Candidate_D}: {percent_vote_D:.3f}% ({total_count_D})')
print(f'{Candidate_R}: {percent_vote_R:.3f}% ({total_count_R})')


# Solving Part 5 "The winner of the election based on popular vote"

if total_count_C > total_count_D and total_count_C > total_count_R:
    winner = Candidate_C
elif total_count_D > total_count_C and total_count_D > total_count_R:
    winner = Candidate_D
else:
    winner = Candidate_R

print(f'Winner: {winner}')


# Output data to a text file

# create new text file called 'output'
with open('output.txt', 'w') as f:
    f.write('Election Results\n')

    f.write('...............................................................\n')

    f.write(f'Total Votes: {total_vote}\n')

    f.write('...............................................................\n')

    f.write(f'{Candidate_C}: {percent_vote_C:.3f}% ({total_count_C})\n')

    f.write(f'{Candidate_D}: {percent_vote_D:.3f}% ({total_count_D})\n')

    f.write(f'{Candidate_R}: {percent_vote_R:.3f}% ({total_count_R})\n')

    f.write('...............................................................\n')

    f.write(f'Winner: {winner}\n')

    f.write('...............................................................\n')

f.close()


