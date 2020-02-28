import os, shutil, re

directory = 'C:/Documents/Sort-Folder'
os.chdir(directory)

filenameRegex = re.compile(r'''
^(.*?)
(\d{3})
(.*?)$
''', re.VERBOSE)

for files in os.listdir(directory):
  mo = filenameRegex.search(files)
  beforePart = mo.group(1)
  digitPart = mo.group(2)
  afterPart = mo.group(3)
  print(f'File found in {path} is {files}')
  print('Need to rename: ' + digitPart + '\n')

newDigitPart = 1
for files in os.listdir(directory):
  newFilename = beforePart + str(newDigitPart).zfill(3) + afterPart
  newDigitPart += 1
  source = os.path.join(directory, files)
  destination = os.path.join(directory, newFilename)


  if newFilename in os.listdir(directory):
    print(f'{newFilename} already exists! Skipping...')
    continue
  else:
    print(f'Renaming {files} to {newFilename}')
    shutil.move(source, destination)
print('\nRenaming Process Done!')
