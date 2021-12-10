import pyinputplus as pyip
 '''such as the blank, limit, timeout, default, allowRegexes, and blockRegexes'''

response = pyip.inputInt(prompt='Enter a number bro: ')
print(response)

# response1 = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# print(response)
# response1 = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
# print(response1)

# prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
# response = pyip.inputYesNo(prompt, yesVal='sí', noVal='no')
# if response == 'sí':

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers) # Return an int form of numbers.


response2 = pyip.inputCustom(addsUpToTen) # No parentheses after addsUpToTen here.
