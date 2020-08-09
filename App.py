import csv
from random import choice as rchoice


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]


pairedArray = []
AllArray = []

with open('Book1.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        AllArray.append(row[0])

while AllArray:
    choice = rchoice(AllArray)
    AllArray.remove(choice)
    pairedArray.append(choice)

QA1, QA2 = split_list(pairedArray, wanted_parts=2)
zipped = zip(QA1, QA2)

with open('output.csv', 'wb') as result_file:
    wr = csv.writer(result_file)
    for row in zipped:
        wr.writerow(row)
