import os
import logging
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO, format = '%(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

#Collect variables to send
target = input('Please input target email:\n')
message = input('Please input intended message:\n')

#Open the browser to hardcoded url
browser = webdriver.Chrome()
browser.implicitly_wait(10)     #Automatically wait 10 seconds if nothing is available
browser.get("https://www.gmail.com/")

#Fill out email then move to next page
identifierForm = browser.find_element_by_id('identifierId')
identifierForm.send_keys('AutotheBoring')
identifierButton = browser.find_element_by_id('identifierNext')
identifierButton.click()

#Fill out password then move onto the next page
passwordForm = browser.find_element_by_name('password')
passwordForm.send_keys('Idontcare')
passwordButton = browser.find_element_by_id('passwordNext')
passwordButton.click()

#Compose the email
    #Press the compose button
composeButton = browser.find_element_by_class_name('z0')
composeButton.click()

    #Fill out the forms
toLine = browser.find_element_by_name('to')
subjectLine = browser.find_element_by_name('subjectbox')

toLine.send_keys(target)
subjectLine.send_keys('Sent by command line :)' + Keys.TAB + message + Keys.TAB + Keys.ENTER)

    #Send and quit the browser

browser.quit()
