'''Saving Variables with the Shelve Module'''
import shelve

#insert
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

#print
# shelfFile = shelve.open('mydata')
# print(type(shelfFile))
# print(shelfFile['cats'])
# shelfFile.close()

#print keys and values
# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()


'''Saving Variables with the PPrint.format() function'''

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)


# fileObj = open('myCats.py', 'w')
# fileObj.write('cats=' + pprint.pformat(cats) + '\n')
# fileObj.close()

import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])
