import os
import bs4
import requests


#Gather url and send it to res to check if it's functional
os.makedirs('Links', exist_ok=True) #Make a directory to save links to
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
while (answer != 'Yes' and answer != 'No' ):
    answer = input("\nDo you want to continue? Yes/No\n")

#Stop the program if the answer was no
if answer == 'No':
    print('Closing program...')
#Else, start running through
else:
    for i in range(soupLen):
        print('Downloading link #' + str(i+1) + '...')
        #link = url + href
        linkRes = requests.get(link)

        #check linkRes
        #if linkRes.status_code == requests.codes.ok
            #then download the href's res.text
            #save the name based on the a's text
        #print notification if it's a 404
