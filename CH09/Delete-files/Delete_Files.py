import os

directory = 'C:\\Users\\DELL\\Desktop\\flash'

folder = os.path.abspath(directory)

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        fileSize = os.path.getsize(foldername + '\\' + filename)
        if int(fileSize) < 100000000:
           continue
           os.unlink(filename)
        print('Deleting ' + filename + '...')


print('Done')
