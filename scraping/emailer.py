from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import pyinputplus as pyip

# email = 'davidstefanusst@gmail.com'
# emailTo = pyip.inputStr(prompt='Enter email to send: ')
# message = pyip.inputStr(prompt='message: ')
# print(emailTo)
# print(message)

browser = webdriver.Chrome(r'C:\Users\david\AppData\Local\Programs\Python\Python38-32\py_development\automate\scraping\chromedriver')
print(browser)
browser.get('https://twitter.com/home')
try:
    username = browser.find_element_by_tag_name('input')
    print('element <%s> found' % (username.tag_name))
except:
    print('Element not found')
time.sleep(100)
browser.quit()


#r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1inuy60 r-utggzx r-vmopo1 r-1w50u8q r-1swcuj1 r-1dz5y72 r-fdjqy7 r-13qz1uu
#r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1inuy60 r-utggzx r-vmopo1 r-1w50u8q r-1swcuj1 r-1dz5y72 r-fdjqy7 r-13qz1uu
#<input autocapitalize="none" autocomplete="on" autocorrect="off" name="session[username_or_email]" spellcheck="false" type="text" dir="auto" data-focusable="true" class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1inuy60 r-utggzx r-vmopo1 r-1w50u8q r-1swcuj1 r-1dz5y72 r-fdjqy7 r-13qz1uu" value="">
#<input autocapitalize="none" autocomplete="on" autocorrect="off" name="session[password]" spellcheck="false" type="password" dir="auto" data-focusable="true" class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1inuy60 r-utggzx r-vmopo1 r-1w50u8q r-1swcuj1 r-1dz5y72 r-fdjqy7 r-13qz1uu" value="">
