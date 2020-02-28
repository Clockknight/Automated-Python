import os
import sys
import PyPDF2

fileList = [] #Initialize array


#Scan for pdf files to encrypt
for root, dirs, files in os.walk('.', topdown = False):
    for name in files:
        if name[-4:] == '.pdf':
            fileList.append(os.path.join(root, name))

for file in fileList:
    print('File found at:\n\t' + file + '\nEncrypting file...\n\n')

    #Encrypt all the files
    pdfFile = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()

    #Add '_encrypted to pdf'
    newFilename = file[:-4] + '_encrypted.pdf'

    #Copy the original pdf to writer, page by page
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    #Encrypt the copy
    pdfWriter.encrypt('swordwish')
    resultPdf = open(newFilename, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

    encryptedPdf = open(newFilename, 'rb')
    newReader = PyPDF2.PdfFileReader(encryptedPdf)

    #Decrypt the new file as a check
    if newReader.decrypt('swordwish') == 1:
        pdfFile.close()
        #Delete the file
        os.remove(file)

    encryptedPdf.close()
