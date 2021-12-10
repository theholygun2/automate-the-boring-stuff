import requests

'''Downloading Files From the web with the Requests Module'''

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

print(res.status_code)
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])

'''Checking for Errors'''
res1 = requests.get('https://inventwithpython.com/page_that_does_not_exist')

try:
    res1.raise_for_status() # always use this
except Exception as exc:
    print('There was a problem: %s' %(exc))

'''Saving Downloaded Files to the Hard Drive'''
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
