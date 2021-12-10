from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip
import time

import requests, bs4 ,sys, os

categoryToSearch = pyip.inputStr(prompt='Search for Something on imgur: ')
browser = webdriver.Chrome(r'C:\Users\david\AppData\Local\Programs\Python\Python38-32\py_development\automate\scraping\chromedriver')
url = 'https://imgur.com/'

os.makedirs('imgurPhotos', exist_ok=True)  # store comics in ./xkcd

browser.get(url)
try:
    searchBoxElem = browser.find_element_by_class_name('Searchbar-textInput')
    print(f'found the element, it is a <{searchBoxElem.tag_name}')

    searchBoxElem.send_keys(categoryToSearch)
    searchBoxElem.submit()

    categoryPageUrl = f'{url}search?q={categoryToSearch}'
    print(categoryPageUrl)
    res = requests.get(categoryPageUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imageLinkElem = soup.find_all('a',{'class': 'image-list-link'})
    imageLink = []
    for link in imageLinkElem:
        print(link.get('href'))
        imageLink.append(link.get('href'))

    res = requests.get('https://imgur.com'+imageLink[0])
    res.raise_for_status()
    print('https://imgur.com'+imageLink[0])
    browser.get('https://imgur.com'+imageLink[0])
    time.sleep(10)

    
    #soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #print(soup)
    #theDiv = soup.find('div',{'class': 'imageContainer zoomable'})
    #print(theDiv)
    # thePicture = theDiv.select('img')[1]
    # picSrc = theDiv.get('src')
    # print(picSrc)

    #imageElem = soup.select('div img')

    # imageElem = soup.find('div', {'class': 'post'})
    # imgSrc = imageElem.find('img')
    # src = imgSrc.find('src')
    # print(imageElem)
    # print(imgSrc)
    # print(src)

except Exception as exx:
    print('element not found')
    print(str(exx))

browser.quit()
