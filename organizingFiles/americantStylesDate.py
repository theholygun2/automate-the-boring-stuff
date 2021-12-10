import re, shutil, os
from pathlib import Path

p = Path.cwd()

datePattern = re.compile(r'''
^(.*?)
((0|1)?\d)-         #one or two digtis for month
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
''', re.VERBOSE)

for amerFileName in os.listdir(p):

    mo = datePattern.search(amerFileName)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

    euroFileName = beforePart + dayPart + monthPart + yearPart + afterPart
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    shutil.move(amerFileName, euroFileName)

print(absWorkingDir)
