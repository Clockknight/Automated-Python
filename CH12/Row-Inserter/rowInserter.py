import os
import sys
import openpyxl
from openpyxl import workbook

#Take 3 argvs
    #first argv is what line is the baseLine
    #second argv is the amount of rows that will be expanded
    #third argv is tharget xlsx file

#Get sheet dimensions

#Copy values down the sheet
    #For loop, i in maxRow - baseLine
    #For loop, j in maxColumn
    #cell(i+baseline+expand, j).value = cell(i+baseline, j).value

#Clear cells for the rows needed
