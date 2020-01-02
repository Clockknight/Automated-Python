import os
import sys
import PyPDF2

processFailure = True

lockedFile = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))



#Read from dictionary.txt
dictFile = open(dictionary.txt, 'r')

for line in dictFile: #For looping through passwords
    password = line[:-2]    #Each line is [:-2], to account for the \n at the end
    print('Trying %s as a password...' % password)
    #Break if decrypt returns 1
    if encryptedReader.decrypt(password) == 1:
        print('Success! The password was %s' % password)
        processFailure = False
        break

    #Don't do anything if it returns 0

#Fail case
if processFailure:
    print('The password was not found in the list given.')
