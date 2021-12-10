#! python3
# combinePdfs.py = Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2, os

#Get all the PDF filenames
pdfFiles = []
# for filename in os.listdir('.')
#     if filename.endswith('.pdf'):
#         pdfFiles.append(filename)
#
# pdfFiles.sort(key=str.lower)
#
# pdfWriter = PyPDF2.PdfFileWriter()

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

print(pdfFiles)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    fileReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, fileReader.numPages):
        pageObj = PdfFileReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open('allpagecombined.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
pdfFileObj.close()
