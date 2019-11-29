#! python3
#   lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(debug)

print('Googling...') #display text while downloading the google page
url = ('http://google.com/search?q=' + 'whale')
res = requests.get(url)
res.raise_for_status()
#logging.debug('res is: ' + res.text)

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
#logging.debug('soup is: ' + str(soup)) 

# TODO: Open a browser tab for each result.
linkElems = soup.find_all(".r a")
for div in linkElems:
    print(div.select("a"))
logging.debug('linkElems = ' + str(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))


#When done, change hardcoded whale back into ' '.join(sys.argv[1:]))
