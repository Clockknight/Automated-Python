from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://mail.aol.com/'

browser = webdriver.Firefox()
browser.get(url)

loginElem = browser.find_element_by_id("lgnId1")
loginElem.send_keys("*****")

passElem = browser.find_element_by_id("pwdId1")
passElem.send_keys("*****")

submitElem = browser.find_element_by_id("submitID")
submitElem.click()

browser.get('https://mail.aol.com/webmail-std/en-us/suite#')

composeElem = browser.find_element_by_class_name("unselectable btn composeBtn")
composeElem.click()
