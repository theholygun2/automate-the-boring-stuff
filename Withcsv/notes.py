import csv

'''Reader Objects'''

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

'''Reading Data from reader Objects in a for loop'''

# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

'''writer Objects'''
# outputFile = open('output.csv','w',newline='')
# outputWriter = csv.writer(outputFile)
# print(outputWriter.writerow(['spam','eggs','bacon','ham']))
# print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))

'''The delimiter and lineterminator Keyword Arguments'''
# csvFile = open('wakwaw.csv','w',newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples','oranges','graped'])
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# csvFile.close()

'''DictReader and DictWriter CSV Objects'''
exampleFile2 = open('exampleWithHeader.csv')

# exampleDictReader = csv.DictReader(exampleFile2)
# for row in exampleDictReader:
#     print(row['Timestamp'], row['Fruit'], row['Quantity'])
#
# exampleDictReader2 = csv.DictReader(exampleFile2, ['time','name','amount'])
# for row in exampleDictReader2:
#     print(row['time'], row['name'], row['amount'])

# output2File = open('output2.csv','w', newline='')
# output2DictWriter = csv.DictWriter(output2File, ['Name','Pet','Phone'])
# output2DictWriter.writeheader()
# output2DictWriter.writerow({'Name': 'Alice', 'Pet': 'Cat', 'Phone': '555-1234'})
# output2DictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
# output2DictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

#output2File.close()
