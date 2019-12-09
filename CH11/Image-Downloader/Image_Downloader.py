import os
import sys
import bs4
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

#Initialize Webdriver to browse imgur
#query =  input('Please input a term to search imgur for:\n')
query = 'meme' #placeholder
queryUrl = 'http://imgur.com/search?q=' + query
os.makedirs(str(query), exist_ok=True)

browser = webdriver.Chrome()
browser.get(queryUrl)
browser.implicitly_wait(2)

#Selenium finds all img elements
images = browser.find_elements_by_class_name('image-list-link')  #find a tag with image-list-link class
results = len(images)

#Skips to end if no images are found.
if results == 0:
    print('No results found.\nClosing program...')
    sys.exit(0)

#Download confirmation
print('Found ' + str(results) + ' images.')
answer = 'Yes' #answer = input('Do you wish to download?\nYes/No\n')
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
            images = browser.find_elements_by_class_name('image-list-link')

            #Use bs4 to scan the result page
            res = requests.get(imageUrl)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, features="lxml")

            #find images with BeautifulSoup
            source = soup.find('link', {'rel': 'image_src', 'href': True}).get('href')
            srcRes = requests.get(source)

            try:
                srcRes.raise_for_status()

                #download image
                imageDownload = open(os.path.join('results', os.path.basename('Result #' + str(1+i)), 'wb'))
                for chunk in srcRes.iter_content(100000):
                    imageDownload.write(chunk)
                imageDownload.close()

            except Exception as exc:
                print('There was a Problem: %s\nSkipping...' % (exc))



        except Exception as exc:
            print('There was a Problem: %s\nSkipping...' % (exc))


#Close the program afterwards
browser.quit()
