from pathlib import Path
import os
print(Path('spam','bacon','eggs')) #print the path object

#print(str(Path('spam','bacon','eggs'))) string

# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(Path(r'C:\Users\AI', filename))

'''Join paths using /, left must be a path object'''
# Path('spam') / 'bacon' / 'eggs'
# Path('spam') / Path('bacon/eggs')
# Path('spam') / Path('bacon', 'eggs')

print(Path.cwd()) #get current directory as a path object

#os.chdir('C:\\Windows\\System32') #change current directory
print(Path.cwd())
print(Path.home()) #return a path home object

'''checking a path is absolute'''
print(Path.cwd().is_absolute())
print(os.path.abspath('.')) #return a string of abs path
print(os.path.isabs('.'))#return true or false it its abs or not


p = Path('C:/Users/Al/spam.txt')
# print(p)
# print(p.anchor, 'anchor')
# print(type(p.anchor))
# print(p.parent, 'parent') # This is a Path object, not a string.
# print(type(p.parent))
# print(p.name, 'name')
# print(p.stem, 'stem')
# print(p.suffix, 'suffix')
# print(p.drive, 'drive')

'''create new 3 directories example'''
#os.makedirs('C:\\asdads\\sdasd\\adasd')
'''Create a directory from a path object'''
# Path(r'C:\Users\AI\spam').mkdir()


'''Get an absolute path from a relative path'''
Path('my/relative/path')
Path.cwd() / Path('my/relative/path')
Path.home() / Path('my/relative/path')

'''Example using os to search both dirname and basename'''
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
#os.path.basename(calcFilePath) #calc.exe
#os.path.dirname(calcFilePath)  #C:\\Windows\\System32

'''path's dir name and base name together to get a tuple value'''
#os.path.split(calcFilePath) #('C:\\Windows\\System32', 'calc.exe')

print(calcFilePath.split(os.sep)) #['C:', 'Windows', 'System32', 'calc.exe']

'''Finding FILE SIZES and Folder Contents'''
print(os.path.getsize(r'C:\Users\david\Documents\Capture.png'))

'''return a list of filename strings for each file in the argument'''
print(os.listdir(r'C:\Users\david\Documents'))

totalSize = 0
for filename in os.listdir(r'C:\Users\david\Documents'):
    totalSize += os.path.getsize(os.path.join(r'C:\Users\david\Documents', filename))
print(totalSize)


'''Modyfying a List of Files Using Glob Patterns'''
z =  Path('C:/Users/David/Documents')
print(type(z.glob('*')))
print(z.glob('*'))

#print(list(z.glob('*')))

'''Print all pdf file in the path'''
#print(list(z.glob('*.PDF')))

'''? means any SINGLE character, 4_22.PDF will not count'''
print(list(z.glob('DavidStefan_4_?.PDF')))
print(list(z.glob('*.?x?')))        #exe txt


for textFilePathObj in z.glob('*.PDF'):
    print(textFilePathObj) #return a path OBJECTTT

'''VALIDATING PATH '''
print(z.exists())
print(z.is_file())
print(z.is_dir())

dDrive = Path('C:/')
print(dDrive.exists())
