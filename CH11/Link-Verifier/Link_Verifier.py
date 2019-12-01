import os
import bs4
import requests

#url = input('Please choose a website to try and download:\n')
url = 'http://google.com'
res = requests. get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="lxml")
linkList = soup.find_all('a')
soupLen = len(linkList)
print("Found " + str(soupLen) + " links in the document")
