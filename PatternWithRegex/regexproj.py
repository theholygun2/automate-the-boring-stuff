import re, pyperclip

matches = []
matches1 = []

phoneRegex = re.compile(r'''(
(\+\d{2})       #kode daerah
(\d{8,12})    #kode belakang
)''',re.VERBOSE)

for groups in phoneRegex.findall('+6281288452215+6887780907248'):
    phoneNum = '-'.join([groups[1], groups[2]])
    matches.append(phoneNum)

if len(matches) > 0:
    #pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    #print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

#4/04/2000


def dateChecker(theDate):
    matches = []
    dayonMonth = {}
    valid = False
    dateRegex = re.compile(r'''(
    (0?[1-9]|[12][0-9]|3\d)/     #day
                      #seperator
    (0?[1-9]|1[0-2])/          #month
                     #seperator
    ([12]\d{3})          #year
    )''', re.VERBOSE)

    #result = dateRegex.findall(theDate)
    #day = result[0][1]

    dayAddRegex = re.compile(r'(^[1-9]$)')
    dateMonthGenapRegex = r'(^[0-2][0-9]|^30)/(0?[468]|10|12)'
    dateMonthGanjilRegex = r'(^[0-2][0-9]|^3[01])/(0?[13579]|11)'
    validateRegex = re.compile(r'%s|%s' %(dateMonthGenapRegex, dateMonthGanjilRegex))

    for groups in dateRegex.findall(theDate):

        day = dayAddRegex.sub(r'0\1', groups[1])
        month = groups[2] #12
        year = groups[3]
        dateMonth = '/'.join([day, month])

    if validateRegex.search(dateMonth): #if there is a value
        print(validateRegex.search(dateMonth))
        matches.append(validateRegex.search(dateMonth))
        valid = True

    return valid

print(dateChecker('40/04/2000'))

def passChecker(password):

        matches = []

        passRules = {'num': r'[0-9]', 'lower': r'[a-z]', 'upper': r'[A-Z]', 'min8': r'.{8,}'}
        for rule in passRules:
            compiled = re.compile(passRules[rule])
            result = compiled.search(password)
            matches.append(result)

        print(matches)
        if None in matches:
            print('password is pretty weak')
        else:
            print('strong')


#passChecker('1')
