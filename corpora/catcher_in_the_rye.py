import PyPDF2
import sys

#sys.setdefaultencoding('utf-8')

pdfFileObj = open('mypdf.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numPages = pdfReader.numPages

myTxt = open('catcher_in_the_rye.txt', 'w')

fullTxt = ""

for i in range(0, numPages):
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extractText()

    pageText = pageText.replace('\n', ' ')

    wow = ' '.join(pageText.split())

    fullTxt += " " + wow

    #print(pageText)

    #myTxt.write(pageText.encode('utf-8'))

print(fullTxt)
myTxt.write(fullTxt.encode('utf-8'))