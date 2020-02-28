import os
import sys
import PyPDF2

#Initializing Variables
fileList = []

#os.walk to find all .pdf files
for root, dirs, files in os.walk('.', topdown = False):
    for name in files:
        if name[-4:] == '.pdf':
            fileList.append(os.path.join(root, name))



#For each one, add them to the list IF they're encrypted
#Take each page from the decrypted file and store it
#Write it to new, unencrypted file
