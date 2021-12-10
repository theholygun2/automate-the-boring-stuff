   #! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

import zipfile, os
from pathlib import Path

p = Path.cwd()

#os.makedirs(p/'delicious'/'cats')
#os.makedirs(p/'walnut'/'waffles')

# print(p/'delicious'/'cats')
# cats = p/'delicious'/'cats'/'catnames.txt'
# cats.write_text('')
# print(p/'walnut'/'waffles')

print(os.path.abspath(p))
print(os.path.basename(p) + ' ' + '1' + '.zip')


def backupToZip(folder):
    folder = os.path.abspath(folder)

    # figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    #Create the zip file
    print(f'Creating {zipFilename}...')

    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        #Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('done...')


def backupYogs(folder):
    folder = os.path.abspath(folder)

    for folderName, subfolders, filenames in os.walk(folder):
