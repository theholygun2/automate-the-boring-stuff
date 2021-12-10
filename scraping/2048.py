from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

url = 'https://gabrielecirulli.github.io/2048/'

browser = webdriver.Chrome(r'C:\Users\david\AppData\Local\Programs\Python\Python38-32\py_development\automate\scraping\chromedriver')
browser.get(url)

htmlElem = browser.find_element_by_tag_name('html')

keysList = ['UP','RIGHT','DOWN','LEFT']
keysList1 = [Keys.UP,Keys.RIGHT,Keys.DOWN,Keys.LEFT]

for i in range(100):
    for y in range(len(keysList)):
        htmlElem.send_keys(keysList1[y])
        time.sleep(1)

time.sleep(3)
browser.quit()
