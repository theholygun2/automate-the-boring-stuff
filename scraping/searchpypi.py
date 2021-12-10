#! python3
# searchpypi.py - Opens several search results.

import requests, webbrowser, bs4, sys
print('searching...')
theUrl = 'https://pypi.org/search/?q='
res = requests.get(theUrl + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
