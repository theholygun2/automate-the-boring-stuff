import re


'''GROUPING'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.') #wwithout parantheses
mo.group(1)
'415'
mo.group(2)
'555-4242'
mo.group(0)
'415-555-4242'
mo.group()
'415-555-4242'

text = 'text: My number is (415)-555-4242.' #with parantheses
regexwithparantheses = re.compile(r'(\(\d\d\d\))?-(\d\d\d-\d\d\d\d)')
mo1 = regexwithparantheses.search(text)

areaCode, mainNumber = mo1.groups()
print('area code: ' + areaCode)
print('main number: ' + mainNumber)

'''GREEDY'''
greedyHaRegex = re.compile(r'(Ha){3,5}') #example 1
mo3 = greedyHaRegex.search('HaHaHaHaHa')
mo3.group()
'''HaHaHaHaHa'''

greedyRegex = re.compile(r'<.*>') #example 2
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
'''<To serve man> for dinner.>'''

'''NON-GREEDY'''
nongreedyHaRegex = re.compile(r'(Ha){3,5}?') #example 1
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
'''HaHaHa'''

nongreedyRegex = re.compile(r'<.*?>')#example 2
mo5 = nongreedyRegex.search('<To serve man> for dinner.>')
mo5.group()
'''<To serve man>'''


"""USING REGEX CLASS"""
vowelRegex = re.compile(r'[aiueoAIUEO]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
'''['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']'''

"""CONSONANT REGEX"""
vowelRegex1 = re.compile(r'[^aiueoAIUEO]')
vowelRegex1.findall('RoboCop eats baby food. BABY FOOD.')
'''['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '', 'B', 'B', 'Y', ' ', 'F', 'D', '.']'''


"""THE CARROT AND DOLLAR SIGN CHARACTERS"""
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, World!') #<re.Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said Hello') == None # TRUE


endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
'''<re.Match object; span=(16, 17), match='2'>'''
print(endsWithNumber.search('Your number is forty two.') == None) #True

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

""" . OR (DOT)"""
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.') #['cat', 'hat', 'sat', 'lat', 'mat']

"""Matching Everything with Dot-Star"""
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo4 = nameRegex.search('First Name: Al Last Name: Sweigart')
mo4.group(1)    #'Al'
mo4.group(2)    #'Sweigart'



'''Matches NewLine with the Dot Character'''
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'''Serve the public trust.\nProtect the innocent.\nUphold the law.'''


'''CASE-SENSITIVE MATCHING'''
robocop = re.compile(r'robocop', re.I) #EXAMPLE 1
robocop.search('RoboCop is part man, part machine, all cop.').group()
'''RoboCop'''
robocop.search('ROBOCOP protects the innocent.').group() #EXAMPLE 2
'''ROBOCOP'''
robocop.search('Al, why does your programming book talk about robocop so much?').group() #EXAMPLE 3
'''robocop'''


'''Substituting Strings with the sub() Method'''
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'''CENSORED gave the secret documents to CENSORED.'''

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))


'''Using Verbose to Managing Complex Regexis'''
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

'''Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE'''
someRegexValue = re.compile('foo', re.IGNORECASE|re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
