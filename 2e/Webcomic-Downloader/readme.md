## Webcomic Downloader:
This script uses webscraping libraries like BeautifulSoup4 and Requests to download the pages of webcomics, like xkcd, or order of the stick. Currently, the code defaults to downloading pages from order of the stick, but should be able to work with other comics in a limited capacity.

### Motivation in making this script:
This script was one of the practice projects in [Automate the Boring stuff with Python]. Writing this code helped develop my understanding of python, and the lesson from the chapter this project was in, specifically how to webscrape to grab files and information efficiently.

### Installation Instructions:
#### Libraries imported:
BeautifulSoup4
requests

Once the above libraries are installed, the program is ready to use like any other script.

### How to use:
This program is intended to be automated, with an initial first running. Just copy the URL of the comic you'd like to download, then run the program. The code will keep track of the url you copied in the target.txt file, so if you're moving the script, be sure to also move target.txt as well.
After that, the recommended way to use this script is to put a shortcut to it inside your startup folder, so it'll check for new pages on whichever comic you chose.
