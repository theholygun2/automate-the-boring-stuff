from pathlib import Path

'''append text to a file'''
baconFile = open('bacon.txt', 'a') #if no file found it will make a new


'''The File Reading/Writing Process'''

p = Path('spam.txt')
#print(p.write_text('Hello World!'))

#print(p.read_text())
'''Opening Files with the open() Function'''
helloFile = open(Path.cwd()/'spam.txt')

'''Reading the Contents of Files'''
helloContent = helloFile.read()
#print(helloContent)

helloFile = open(Path.cwd()/'spam.txt')
print(helloFile.readlines()) #this will return a list object
