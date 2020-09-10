import re
import os

i = 0
j = 0
term = ''
matches = []
lines = []

allFile = os.listdir('.')#Find all files in the folder
files = len(allFile)

term = input('Please input a term to find in the files: ')

#print(allFile)
while i < files:
    #print(allFile[i])
    currentFile = open('./' + allFile[i])
    lines = list(currentFile)
    print(lines)
    #print("pass" + str(i))
    checkRegex = re.compile(r'(.txt)$')
    mo = checkRegex.search(allFile[i])
    if mo != None:
        for line in lines:
            currentRegex = re.compile(r'(%s)'%term, re.I)#Search each line.
            mo = currentRegex.search(line)
            mo.group()
            print(line)
    i += 1
