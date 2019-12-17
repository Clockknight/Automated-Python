import os
import sys
import openpyxl
from openpyxl import workbook

#Take 3 argvs
    if len(sys.argv) != 4 or str(sys.argv[3][-5:]) != '.xlsx':
        print("Input arguments were invalid. Please make sure that the input looks something like:\n\trowInserter.py 3 4 too_Compact.xlsx\n\tWhere the two integers are the rows you don't want moved, and the amount of rows you want the rest of the sheet moved down, respectively.")
    #first argv is what line is the baseLine
    #second argv is the amount of rows that will be expanded
    #third argv is tharget xlsx file


#Get sheet dimensions
sheetWidth = sheet.max_column
sheetHeight = sheet.max_row
if sys.argv[1] >= sheetHeight:
    print("Your first integer was too great. There are only %d rows in %s." % (sheetHeight,str(sys.argv[3])))

#Copy values down the sheet
    #For loop, i in maxRow - baseLine
    #For loop, j in maxColumn
    #cell(i+baseline+expand, j).value = cell(i+baseline, j).value

#Clear cells for the rows needed
