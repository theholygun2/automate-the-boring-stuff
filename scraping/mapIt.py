import webbrowser, sys, pyperclip
import requests


if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print('Going to: ' + address)
webbrowser.open('https://www.google.com/maps/place/' + address)
