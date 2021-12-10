from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'C:\Users\david\AppData\Local\Programs\Python\Python38-32\py_development\automate\scraping\chromedriver')
print(browser)
# browser = webdriver.Chrome()
# browser.get('http://google.com')



browser.get('http://www.google.com/')
#time.sleep(3) # Let the user actually see something!
search_box = browser.find_element_by_name('q')
search_box.send_keys('smbfunny instagram')
search_box.submit()
time.sleep(3) # Let the user actually see something!
try:
    elem = browser.find_element_by_class_name('')
    print('Found <%s> element with that class name!' % (elem.tag_name))


except:
    print('Was not able to find an element with that name.')
browser.quit()


# service = Service(r'C:\Users\david\AppData\Local\Programs\Python\Python38-32\py_development\automate\scraping\chromedriver')
# service.start()
# driver = webdriver.Remote(service.service_url)
# driver.get('http://www.google.com/');
# time.sleep(5) # Let the user actually see something!
# driver.quit()


'''Clicking the Page'''
# print(type(browser))
# browser.get('https://inventwithpython.com')
#
# try:
#     elem = browser.find_element_by_class_name(' cover-thumb')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')
#
#
# linkElem = browser.find_element_by_link_text('Read Online for Free')
# linkElem.click()

'''Filling Out and Submitting Forms'''
# browser.get('https://login.metafilter.com')
# userElem = browser.find_element_by_id('user_name')
# userElem.send_keys('your_real_username_here')
#
# passwordElem = browser.find_element_by_id('user_pass')
# passwordElem.send_keys('your_real_password_here')
# passwordElem.submit()

'''Sending Special Keys'''
# browser.get('https://nostarch.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)  #scroll to bottom
# htmlElem.send_keys(Keys.HOME) #scrolls to top

'''Clicking Browser Buttons'''
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()
