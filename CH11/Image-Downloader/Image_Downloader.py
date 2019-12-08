import os
import sys
import bs4
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

#Initialize Webdriver to browse imgur
#query = 'http://imgur.com/search?q=' + input('Please input a term to search imgur for:\n')
queryUrl = 'http://imgur.com/search?q=meme' #placeholder

browser = webdriver.Chrome()
browser.get(queryUrl)
browser.implicitly_wait(2)

#Selenium finds all img elements
images = browser.find_elements_by_class_name('image-list-link')  #find a tag with image-list-link class
results = len(images)

#Skips to end if no images are found.
if results == 0:
    print('No results found.\nClosing program...')

#Download confirmation
else:
    print('Found ' + str(results) + ' images.')
    answer = input('Do you wish to download?\nYes/No\n')
    while (answer != 'Yes' and answer != 'No'):
        answer = input('\nInvalid answer, this program only reads either Yes or No.\nDo you wish to download?\nYes/No\n')
    if answer == 'No':
        print('Okay. Shutting down...')
    else:
        for i in range(results):
            print('Downloading image #' + str(i+1) + '...')
            try:
                #Go to the ith image
                currentImage = images[i]
                currentImage.send_keys(Keys.ENTER)
                imageUrl = browser.current_url
                browser.get(queryUrl)

                #Use bs4 to scan the image
                res = requests.get(imageUrl)
                res.raise_for_status()
                soup = bs4.BeautifulSoup(res.text)
                #find image with BeautifulSoup
                #download image
            except:
                print('Bad download. Skipping...')



#Close the program afterwards
browser.quit()
sys.exit(0)
