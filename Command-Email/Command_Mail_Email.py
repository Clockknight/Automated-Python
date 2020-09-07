import os
import logging
import re
import selenium
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format = '%(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

#Collect variables to send
target = input('Please input target email:\n')
message = input('Please input intended message:\n')

#Open the browser to hardcoded url
browser = webdriver.Chrome()
browser.get("https://www.mail.com/")

#Find and click the button
loginButton = browser.find_element_by_id('login-button')
loginButton.click()
browser.implicitly_wait(30)

#Find and fillout the login & password areas
loginForm = browser.find_element_by_name('username')
passwordForm = browser.find_element_by_name('password')
submitButton = browser.find_element_by_class_name('login-submit')
composeLink = browser.find_element_by_css_selector('div.buttons a.button-signup')
logging.info(composeLink.get_attribute('value'))

loginForm.send_keys('AutotheBoring')
passwordForm.send_keys('Idontcare')
submitButton.click()

'''#Go to barrier free inbox
currentUrl = browser.current_url
sIDRegex = re.compile(r'(?sid)(.)')
sIDMatch = sIDRegex.search(currentUrl)
logging.debug(sIDMatch.group())

#go to https://navigator-lax.mail.com + found href
browser.get('https://navigator-lax.mail.com' + scraperUrl)'''

#Compose the email
composeLink.click()

'''
toLine = browser.find_element_by
subjectLine = browser.find_element_by
emailBody = browser.find_element_by
sendButton = browser.find_element_by

toLine.send_keys(target)
subjectLine.send_keys('Sent by command line :)')
emailBody.send_keys(message)

sendButton.click()'''
#
browser.close()

