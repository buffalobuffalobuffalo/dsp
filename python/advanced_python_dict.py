import csv
from collections import Counter
import re


with open('faculty.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    
    namelist = []
    degreelist = []
    emaillist = []
    positionlist= []
    statslist = []
    
    for row in csv_reader:
        namelist.append(row[0])
        degreelist.append(row[1])
        positionlist.append(row[2])
        emaillist.append(row[3])
        statslist.append([row[1],row[2],row[3]])
    
    lastnamelist = []
    for name in namelist:
        lastname = name.split()[-1]
        lastnamelist.append(lastname)
    
    position2 = []
    for position in positionlist:
        if position.startswith('Asso'):
            position2.append('Associate Professor')
        elif position.startswith('Assi'):
            position2.append('Assistant Professor')
        else:
            position2.append('Professor')

# cleaning up the degree lists    
    newdegreelist = []
    for item in degreelist:
        nospace = item.strip()
        newdegreelist.append(nospace)
    
    newerdegreelist = []
    for item in newdegreelist:
        if item.startswith('P'):
            newerdegreelist.append('PhD')
        else:
            degree = item.split(' ',1)
            newerdegreelist.append(degree[0])
    
    values = zip(newerdegreelist,position2,emaillist)
    
    faculty_dict = dict(zip(lastnamelist, values))
  
#    faculty_dict is the answer to q1
    print faculty_dict

    
    firstnamelist = []    
    for name in namelist:
        firstname = name.split()[0]
        firstnamelist.append(firstname)
        
    nametuple = tuple(zip(firstnamelist, lastnamelist))
    fullname_dict = dict(zip(nametuple,values))

#   fullname_dict is answer to q2
    print fullname_dict
        
    keylist = sorted((fullname_dict.keys()), key = lambda x: x[1])
    
#   this function is the answer to q3    
    for key in keylist:
        print "%s: %s" % (key, fullname_dict[key])
