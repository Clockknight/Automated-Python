import os
import sys
import openpyxl
from openpyxl import workbook

#Check rows and columns on the spreadsheet, only actually run if either are 2 or more
    #Take spreadsheet based on argv from cwd
    #Take rows and columns

#Check which dimension is larger, width or  height.
    #Compare, change dimension to width, then height if height > width

#For each row, invert cells equal to current row - 1 (row # 5 will invert 4 cells with column 5)
    #For loop, i in dimension
    #Nested For loop, j in dimension - 1
    #Take value of cell in (i, j), store as sourceValue
    #Take value of cell in (j, i), store as targetValue
    #cell(j, i).value = sourceValue
    #cell(i, j).value = targetValue
