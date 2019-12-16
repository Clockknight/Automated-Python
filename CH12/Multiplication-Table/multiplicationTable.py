import os
import sys
import openpyxl

#Take number N from command line
if len(sys.argv) != 2:
    print("Sorry, this program requires you to pass an additional argument specifying the dimensions of the multiplication square.\nTry:\n\tmultiplicationTable.py 5 for a 5x5 table, etc...")
    sys.exit()

width = int(sys.argv[1])
print("Creating a %dx%d table..." % (width, width))


#Print out NxN multiplication Tabulates

#Bold Row 1 & Column A
