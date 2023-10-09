# python-challenge
Module 3 Challenge

Module 3 Challenge PyBank:

Most if not all data was adapted from the activites done in class with a few key exceptions listed below:

The code setup for finding the Net total amount of Profit/Losses using the "Try:" and "Except/Pass" came from the website: https://stackoverflow.com/questions/11310248/find-number-of-columns-in-csv-file

When solving for the average of changes for Profit/Losses the formula for the problem came from the website: https://careerkarma.com/blog/python-average/

the set up for the problem of solving for the average changes for Profit/Losses :(listed below) was adapted from the website: https://stackoverflow.com/questions/53474110/python-determine-change-in-value-from-one-period-to-the-next
    
     
     for row in csv_reader:
        pl.append(int(row[1]))
        length.append(row[0])
    # Solve for average change
    for i in range(1, len(pl)):
        change.append((int(pl[i]) - int(pl[i-1])))
    
    pl_average = sum(change) / len(change)


Module 3 Challenge PyPoll:

Almost all of the data was adapted from the activites done in class with a key exception listed below:

Using Chat GPT I had the AI adapt my previous output creation code to fit with the formatting of outputs in the PyPoll Challenge (When trying to adapt the code myself using previous format of PyBank I kept getting multiple errors) thus it produced the following code using a "with open" function:


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

