import os
import sys
import bs4
import requests

#Gather url and send it to res to check if it's functional
os.makedirs('Links', exist_ok=True) #Make a directory to save links to
url = input('Please choose a website to try and download (don't forget to put http:// at the start):\n')
res = requests.get(url)
res.raise_for_status()

#Gather <a> tags from the site
soup = bs4.BeautifulSoup(res.text, features="lxml")
linkList = soup.find_all('a')
soupLen = len(linkList)

#Confirm download
if soupLen == 0:
    print("No a tags found on the linked site.\n\nNow closing...")
    sys.exit(0)
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
        link = linkList[i]['href']
        name = linkList[i].text    #Store the a tag text as a variable

        #Change any href that refer to local links
        if (link[:7] != 'http://' and link [:8] != 'https://'):
            link = url + link
        linkRes = requests.get(link)

        #check linkRes and download if there's no error.
        try:
            linkRes.raise_for_status()  #Check for any errors

            #Save the html file to ./Links
            htmlFile = open(os.path.join('Links', os.path.basename(name)), 'wb')
            for chunk in linkRes.iter_content(100000):
                htmlFile.write(chunk)
            htmlFile.close()

        except Exception as exc:
            print('Bad download, skipping...')
