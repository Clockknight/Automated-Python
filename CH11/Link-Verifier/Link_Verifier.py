import os
import bs4
import requests

#Gather url and send it to res to check if it's functional
#url = input('Please choose a website to try and download (don't forget to put http:// at the start):\n')
url = 'http://google.com'
res = requests. get(url)
res.raise_for_status()

#Gather <a> tags from the site
soup = bs4.BeautifulSoup(res.text, features="lxml")
linkList = soup.find_all('a')
soupLen = len(linkList)

#Confirm download
print("Found " + str(soupLen) + " links at " + url + ".\n")
answer = input("Do you want to continue? Yes/No\n")
while (answer != 'Yes' and 'No' ):
    answer = input("\nDo you want to continue? Yes/No\n")

#
