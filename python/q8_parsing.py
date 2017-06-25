# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('football.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    
    goaldiflist = []
    teamnames = []
    for row in csv_reader:
        teamnames.append(row[0])
        goaldif = (int(row[5]) - int(row[6]))
        goaldiflist.append(goaldif)
    
    goaldifdict = dict(zip(goaldiflist,teamnames))
    
    ans = min(goaldiflist, key=abs)
    print(goaldifdict.get(ans))
    print ans
