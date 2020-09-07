import os
import shutil

typeVariable = ''
sourceDir = ''
destinationDir = ''

typeVariable = '.' + input('Please input a file type:')
print("The file type you're looking for is " + typeVariable )

sourceDir = input("\nPlease input the full directory of the folder tree you'd like to examine and copy files from:\n(Something like C:/Folder/Subfolder/Destination)")
print("The directory of the folder tree you'd like examined is " + sourceDir)

destinationDir = input("\nPlease input the full directory of the destination you'd like the copied files to arrive in:")
print("The destination directory is: " + destinationDir)

print("\n Beginning copy process...")


for folders, subfolders, filenames in os.walk(sourceDir):

    for filename in filenames:

        if filename.endswith(typeVariable):
            shutil.copy(os.path.join(folders, filename), destinationDir)

print("\nCopy completed. All" + typeVariable + "files from " + sourceDir + " have been transferred to " + destinationDir +"".")
