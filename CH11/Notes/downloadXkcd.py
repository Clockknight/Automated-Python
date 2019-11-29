#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4, re

url = 'https://xkcd.com/1525/'             #starting url
os.makedirs('xkcd', exist_ok=True)  #store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            reComicUrl = re.search("imgs.xkcd.com", comicUrl) #Code checks for images that don't start in imgs.xkcd.com
            if reComicUrl == None: #If it wasn't from there...
                prevLink = soup.select('a[rel="prev"]')[0]
                url = 'http://xkcd.com' + prevLink.get('href')
                continue #...skip the comic
            #Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #Skip the comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        
        #Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
