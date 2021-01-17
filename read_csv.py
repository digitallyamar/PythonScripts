import csv

with open('Namekarna_Available.csv', 'r') as fcsv:
    rdr = csv.DictReader(fcsv, delimiter=',')
    for row in rdr:
        print (row['name'])
        break