import re, os
from pathlib import Path

thePath = Path('C:/Users/david/Documents')

print(thePath.exists())
theRegex = input('enter your regex here: ')
theRegex = re.compile(theRegex)
matchList = []

for theFile in thePath.glob('*.txt'):
    fileTxt = open(theFile)
    while True:
        lineToCompare = fileTxt.readline()
        if lineToCompare == '':
            break
        result = theRegex.search(lineToCompare)

        if(result):
            matchList.append(lineToCompare)

print(matchList)
