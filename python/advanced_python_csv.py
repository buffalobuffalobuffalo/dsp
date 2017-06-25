import csv

with open('faculty.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    
    emaillist = []
    for row in csv_reader:
        emaillist.append(row[3])

csvemailfile = 'emails.csv'

with open(csvemailfile, 'w') as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in emaillist:
        writer.writerow([val])
