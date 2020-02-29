import os
import sys
import csv
import openpyxl
from openpyxl import workbook

def main():
    # 1) Read all excel sheets in CWD
    for root, dir, file in os.walk(os.getcwd(), topdown = False):
        for fileName in file:
            if fileName[-5:] == '.xlsx':
                convert(root, fileName)


def convert(root, excelName):
    fileRootName = excelName[:-5]
    csvName = fileRootName + '.csv'
    output = os.path.join(root, csvName)

    # 2) Output all as csv files


    # 3) 1 csv file per excel sheet
    # 4) Titled <filename>_<sheetname>.csv

main()
