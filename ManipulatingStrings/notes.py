'''Escape Characters'''

'''Raw Strings'''
print(r'That is Carol\'s cat.')


'''--Multiline Strings with Triple Quotes--'''
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')


'''--Multiline Comment--'''
def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

'''Indexing and Slicing String'''
spam = 'Hello, World'
fizz = spam[0:5] # output = Hello
print(spam[0]) #'H'
print(fizz)

'''The in and not in Operators with Strings'''
print('Hello' in 'Hello, World') # true
print('Hello' in 'Hello') # True
print('HELLO' in 'Hello, World') # false
print('' in 'spam') # True
print('cats' not in 'cats and dogs') # False

'''Putting Strings Inside Other Strings'''
name = 'Al'
age = 4000
print(My name is %s. I am %s years old.' % (name, age))

name = 'Al'
age = 4000
print(f'My name is {name}. Next year I will be {age + 1}.'
'My name is Al. Next year I will be 4001.')


'''---USEFULL STRING METHODS---'''

'''The upper(), lower(), isupper(), and islower() Methods'''
spam = 'Hello, world!'
spam = spam.upper()
print(spam)
'HELLO, WORLD!'
spam = spam.lower()
print(spam)

print('12345'.islower()) # FALSE
print('12345'.isupper()) # FALSE


'''The isX() METHOD'''
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> '    '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle()
False


'''The startswith() and endswith() Method'''
>>> 'Hello, world!'.startswith('Hello')
True
>>> 'Hello, world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
True
False
>>> 'Hello, world!'.startswith('Hello, world!')
True
>>> 'Hello, world!'.endswith('Hello, world!')


'''The join() and split() Methods'''
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'

>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']


'''Splitting Multiline String with \n'''
>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the
fridge', 'that is labeled "Milk Experiment."', '', 'Please do not drink it.',
'Sincerely,', 'Bob']


'''Splitting Strings with the partition() Method''' # return 3 parameter
>>> 'Hello, world!'.partition('w')
('Hello, ', 'w', 'orld!')
>>> 'Hello, world!'.partition('world')
('Hello, ', 'world', '!')

>>> before, sep, after = 'Hello, world!'.partition(' ') # example of initializing 3 variable at once usually used for before, sep, after
>>> before
'Hello,'
>>> after
'world!'


'''Justifying Text with the rjust(), ljust(), and center() Methods'''
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.ljust(10)
'Hello      '

'''Removing Whitespace with the strip(), rstrip(), and lstrip() Methods'''
>>> spam = '    Hello, World    '
>>> spam.strip()
'Hello, World'
>>> spam.lstrip()
'Hello, World    '
>>> spam.rstrip()
'    Hello, World'

'''Numeric Values of Characters with the ord() and chr() Functions'''
>>> ord('A')
65
>>> ord('4')
52
>>> ord('!')
33
>>> chr(65)
'A'
