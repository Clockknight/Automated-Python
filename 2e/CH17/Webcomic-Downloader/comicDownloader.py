import os
import bs4
import requests

def downloadPage(inputSoup, iterCount):

    imageList = inputSoup.select('img')
    sourceList = []
    source = ''
    comicUrl = ''

    for image in imageList:
        source = image.get('src')
        if source[:36] == 'https://i.giantitp.com//comics/oots/':
            comicUrl = source[36:]

            #Save the image to ./Order Of The Stick.
            #Only
            if iterCount > 25:
                print('Downloading ' + comicUrl + '...')
                iterCount = 0

            res = requests.get(source)
            imageFile = open(os.path.join('Order Of the Stick', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

            return iterCount

#Self iterating function to download all pages after initial Page
def downloadNext(inputSoup, iterCount):

    #Keep track of the iterations that have occured
    iterCount += 1
    confirmedHref = ''
    imgTags = []

    #Download the comic
    downloadPage(inputSoup, iterCount)


    #Find 'next button'
        #Find all a tags with img tags
    aTags = inputSoup.select('a')
        #Select all img tags within
    for tag in aTags:
        result = ''

        imgTags.append(result)
        #Select each img tag
        #Find the one with the next comic title
        #Find the matching a
        #Pull that a tag's href
    pageLink = confirmedHref

    #Find where it's directing to

    #make that the target of nextSoup soup object
    res = requests.get(nextPage)

    if nextSoup == inputSoup:
        return pageLink
    else:
        return downloadNext(nextSoup, iterCount)

def main():
    #Main function is for Initializing files, links, and variables that depend on those links
    #Initializing variables
    inclusiveInt = 0
    file = './target.txt'
    infoArray = []

    #Creating the directory where comic pages will be stored
    os.makedirs('Order Of the Stick', exist_ok=True)

    #Pull a target url if there are any, from inside the file
    target = open(file, 'r+')
    targetInfo = target.read()
    target.close()

    #If the info array pulls no text, then assume default url
    if targetInfo == '':
        print('No link found in target.txt. Taking default url.')
        url = 'https://www.giantitp.com/comics/oots0001.html'

    else:
        #If there is a VALID link in the file, the code will take that and will not download that same page again.
        if targetInfo[:36] == 'https://www.giantitp.com/comics/oots':
            print('Link found in target.txt. Using that url to download pages.')
            #If a link is found, it means that page has already been read, so that comic will not be downloaded
            inclusiveInt = -1
            url = targetInfo[:-1]

        #Otherwise, the code will assume the default url.
        else:
            print('Link in target.txt directs to an invalid link.')
            url = 'https://www.giantitp.com/comics/oots0001.html'

    print('Link obtained. It points to: ' + url)

    #Codeblock to actually begin the code
    #Go to URL
    res = requests.get(url)

    #Obtain current page's soup
    try:
        res.raise_for_status()
        initialSoup = bs4.BeautifulSoup(res.text, 'html.parser')

        #Download current page's comic
        url = downloadNext(initialSoup, 0)


    #Exception clause
    except Exception as exc:
        print('There was problem: %s' % (exc))

    #Finish the program
        #Update target.txt

main()

'''
Sandbox Codeblock

url = 'https://www.giantitp.com/comics/oots0001.html'
testList = [1, 2, 3]
res = requests.get(url)
testSoup = bs4.BeautifulSoup(res.text, 'html.parser')
testMistake = testSoup.select('blblblb')
testList.append(testMistake)
print(testMistake)
print(type(testMistake))
if len(testMistake) == 0:
    print('Test complete')
'''
