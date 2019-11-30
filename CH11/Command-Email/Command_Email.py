import os
import logging
import selenium
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG, format = '%(levelname)s - %(message)s')
#logging.disable(Debug)

#Collect variables to send
target = input('Please input target email:\n')
logging.debug(target)
message = input('Please input intended message:\n')
logging.debug(message)

#Open the browser to hardcoded url
browser = webdriver.Chrome()
browser.get("https://www.mail.com/")

#Find and click the button
loginButton = browser.find_element_by_id('login-button')
loginButton.click()

#Find and fillout the login & password areas
loginForm = browser.find_element_by_name('username')
