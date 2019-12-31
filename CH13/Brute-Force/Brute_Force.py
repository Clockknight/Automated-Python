import os
import sys
import PyPDF2

success = 0
lockedFile = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))

#Read from dictionary.txt
dictFile = open(dictionary.txt, 'r')

for line in dictFile: #For looping through passwords
    password = dictionary[word][:-2]    #Each line is [:-2], to account for the \n at the end

    #Break if decrypt returns 1
    if encryptedReader.decrypt(password) == 0:
        print('Success! The password was %s' % password)
        success = 1
        break

    #Don't do anything if it returns 0

#Fail case
if success == 0:
    print('The password was not found in the list given.')
