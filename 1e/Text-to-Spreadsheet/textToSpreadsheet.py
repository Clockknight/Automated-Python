import os
import sys
import openpyxl
from openpyxl import Workbook

fileCount = 0
book = Workbook()
sheet = book.active

#On startup, ask user for files. Answer "EXIT PROGRAM" once you have selected the files you want to.
#A few outcomes:
while True:
    target = input('\nPlease input name of file to be converted.\nAlternatively, input \'EXIT PROGRAM\' when you\'re done.:\n\t')
    path = './'+target
    #File found, process it and keep track of how many files have been processed
    if os.path.exists(path) == True:
        fileCount += 1
        file = open(path, 'r')

        print('File found. Beginning conversion #%d' % fileCount)

        #Use readlines() to get a list of strings
        fileLines = file.readlines()
        print('File %s has %d lines in it. Converting now...' % (target,len(fileLines)))

        #Make values = the appropriate index in the string thru a for loop
        for i in range(0, len(fileLines)):
            sheet.cell(row=i+1, column=fileCount).value = fileLines[i]


    #EXIT PROGRAM, leave and save the spreadsheet
    elif target == 'EXIT PROGRAM':
        print('Thank you, closing program...')
        book.save(filename = str(fileCount) + 'file textToSpreadsheet.xlsx')
        sys.exit()

    #File not found, try again
    elif os.path.exists(path) == False:
        print('File not found. Try again.')
