import shutil, os
from pathlib import Path
p = Path.cwd()

#print(Path.home())


# ➊ >>> shutil.copy(p / 'spam.txt', p / 'some_folder')
#    'C:\\Users\\Al\\some_folder\\spam.txt'
# ➋ >>> shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
#    WindowsPath('C:/Users/Al/some_folder/eggs2.txt')

#shutil.copytree(source, destination) #copy folder
# shutil.copytree(p / 'spam', p / 'spam_backup')

'''Moving and Renaming Files and folders'''
#shutil.move(source, destination)  #if there is an existing file it will be OVERWRITTTEN

#os.unlink(path)            #detele a file in path
#os.rmdir(path)             #delete a EMPTY FOLDER in path must be empty
#shutil.rmtree(path)        #delete a path entire folder

'''Save Deletes with the send2trash module'''

# import send2trash
# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable')
#
# baconFile.close()
# send2trash.send2trash('bacon.txt')

'''Walking a Directory Tree(rename every file in some folder and also every file in every subfolder)'''

#os.walk returns lists of strings for the subfolder and filename variables
print('')

for folderName, subfolders, filenames in os.walk('C:\\TestFolder'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

'''Compressing Files with the Zipfile Module'''

'''Reading Zip FILES'''

import zipfile

# exampleZip = zipfile.ZipFile(p/'organizingFiles_1.zip')
# print(exampleZip.namelist())
# # spamInfo = exampleZip.getinfo('spam.txt')
# # print(spamInfo.file_size)
# # print(spamInfo.compress_size)
# # print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)} x smaller!')
# exampleZip.close()

'''Extracting from Zip Files'''
#The extractall() method for ZipFile objects extracts all the files and folders from a ZIP file into the current working directory.(EXTRACT ALL FILE FROM THE ZIP)

# exampleZip2 = zipfile.ZipFile(p/'Documents/good.zip')
# exampleZip2.extractall()
# exampleZip2.close()

#The extract() method for ZipFile objects will extract a single file from the ZIP file.(EXTRACT A SINGLE FILE FROM A ZIP)
# exampleZip2.extract('blabla.txt')
# exampleZip2.extract('blabla.txt', 'C:\\some\\new\\folders')
# exampleZip2.close()

'''Creating and Adding to Zip Files'''

# newZip = zipfile.ZipFile('new.zip','w') #creating a zip file named new
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) #adding spam.txt to new.zip
# newZip.close()
# newZip = zipfile.ZipFile('newZip'. 'a') # adding a file to the zip
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) #adding spam.txt to new.zip

#If you want to simply add files to an existing ZIP file, pass 'a' as the second argument to zipfile.ZipFile() to open the ZIP file in append mode.
