import sys, re, os, requests, bs4

def downloadImage(siteURL, category):

    os.makedirs(category, exist_ok=True)

    res = requests.get(siteURL + "/search?q=" + category)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    reg = re.compile(r'(.*?)b(.jpg)$')
    images = soup.select('#imagelist img')
    for img in images:
        if img.get("alt") == "":
            source = img.get("src")
            mo = reg.search(source)
            if mo != None:
                newSource = mo.group(1) + mo.group(2)
                newSource = "https:" + newSource


                imageFile = open(os.path.join(category, os.path.basename(newSource)), "wb")
                res = requests.get(newSource)
                res.raise_for_status
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

    print("Completed)


url = "https://imgur.com/"
category = "progresspics"
downloadImage(url, category)
