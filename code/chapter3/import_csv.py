import csv
import pprint 

csvFile = open('../../data/chapter3/data-text.csv')
#reader = csv.reader(csvFile)
reader = csv.DictReader(csvFile)

for row in reader:
    pprint.pprint(row)