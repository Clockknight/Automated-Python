import bs4
import requests

inclusiveBool = True
file = './target.txt'
infoArray = []

target = open(file, 'r+')
infoArray = target.readlines()

if len(infoArray) == 0:
    print('No link found in target.txt. Taking default url.')
    url = 'https://www.giantitp.com/comics/oots0001.html'

else:
    if infoArray[0][:36] == 'https://www.giantitp.com/comics/oots':
        print('Link found in target.txt. Using that url to download pages.')
        inclusiveBool = False
        url = infoArray[0]

    else:
        print('Link in target.txt directs to an invalid link.')
        url = 'https://www.giantitp.com/comics/oots0001.html'

print('Link obtained. It points to: ' + url)

#Go to URL
res = requests.get(url)
try:
    res.raise_for_status()

except Exception as exc:
    print('There was problem: %s' % (exc))
#Find Next Page Button

#Check if url points to the same url that the site is currently on

#If not, download image to desktop
    #Image should be '''https://i.giantitp.com//comics/oots/oots...'''
    #Then move to the next page

#Save in cwd
