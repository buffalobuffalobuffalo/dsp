import csv
from collections import Counter
import re

with open('faculty.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    
    degreelist1 = []
    positionlist = []
    emaillist = []
    
    for row in csv_reader:
        degreelist1.append(row[1])
        positionlist.append(row[2])
        emaillist.append(row[3])

# determining the number of frequency of degrees
    degreelist2 = [words for segments in degreelist1 for words in segments.split()] 
    degreedict = Counter(degreelist2)
    del degreedict['0']

    degreestring = ' '.join(degreelist2)
    
    phdcount = re.findall(r'[P][.]*[h][.]*[D][.]*', degreestring)
    scdcount = re.findall(r'[S][.]*[c][.]*[D][.]*', degreestring)
    mscount = re.findall(r'[M][.]*[S][.]*', degreestring)
    
#    answer to q1 of p I
    print degreedict
    
    print "but there are some obvious duplicate types,\nso the real numbers are:"
    print 'PhD:', len(phdcount)
    print 'ScD:', len(scdcount)
    print 'MS:', len(mscount)
 
# determining the number and frequency of positions, q2    
    positionstring = ' '.join(positionlist)
    postypelist = []
    
    for item in positionlist:
        title = item.split(' of')
        postypelist.append(title[0])
        
    positions = Counter(postypelist)
   
# answer to q2 of part I
    print positions
    
        
## answer to q3 of part I
    print emaillist

# q4 calculation

    emailstring = ' '.join(emaillist)
    domainlist = re.findall(r'\@(\S*)', emailstring)    
    emaildict = Counter(domainlist)
    
# answer to q4 of part I
    print len(emaildict.keys())
    print emaildict.keys()
