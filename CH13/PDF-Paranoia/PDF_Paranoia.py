import os
import sys
import PyPDF2

fileList = [] #Initialize array


#Scan for pdf files to encrypt
for root, dirs, files in os.walk('.', topdown = False):
    for name in files:
        if name[-4:] == '.pdf':
            fileList.append(os.path.join(root, name[:-4]))

for file in fileList:
    #Encrypt all the files
    print(file)
    #Add '_encrypted to pdf'
