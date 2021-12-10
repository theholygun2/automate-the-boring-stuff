import requests, webbrowser, bs4, sys

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))
# #print(noStarchSoup)


'''Finding an Element with the select() Method'''
# soup.select('div')
# soup.select('')
# soup.select('#author')

# The element with an id attribute of author
#
# soup.select('.notice')
#
# All elements that use a CSS class attribute named notice
#
# soup.select('div span')
#
# All elements named <span> that are within an element named <div>
#
# soup.select('div > span')
#
# All elements named <span> that are directly within an element named <div>, with no other element in between
#
# soup.select('input[name]')
#
# All elements named <input> that have a name attribute with any value
#
# soup.select('input[type="button"]')
#
# All elements named <input> that have an attribute named type with value button


exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(exampleSoup)
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)

print('')

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(str(pElems[0].getText()))

print(str(pElems[1]))
print(str(pElems[1].getText()))

print(str(pElems[2]))
print(str(pElems[2].getText()))
print(len(pElems))

print('')
'''Getting Data from an Element's Attributes'''
soup = bs4.BeautifulSoup(open('example.html'),'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)
print(len(spanElem))
