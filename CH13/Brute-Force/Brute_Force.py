import os
import sys
import PyPDF2

passwordIteration = 0

processFailure = True

encryptedFile = open('.\\encryptedminutes.pdf', 'rb')
encryptedReader = PyPDF2.PdfFileReader(encryptedFile)

dictFile = open('.\\dictionary.txt', 'r')#Read from dictionary.txt

for item in dictFile: #For looping through passwords
    password = item[:-1]    #Each line is [:-2], to account for the \n at the end
    passwordIteration += 1
    if (passwordIteration % 25) == 0:
        print('Testing password #%d, [%s]' % (passwordIteration, password))

    #Break if decrypt returns 1
    if encryptedReader.decrypt(password) == 1:
        print('Success! The password was %s, on line #%d' % (password, passwordIteration))
        processFailure = False
        break

    #Don't do anything if it returns 0

#Fail case
if processFailure:
    print('The password was not found in the list given.')
