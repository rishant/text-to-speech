# https://www.geeksforgeeks.org/convert-pdf-file-text-to-audio-speech-using-python/
# https://www.journaldev.com/33281/pypdf2-python-library-for-pdf-files

# Step:1 - Install pychan IDE for development

# Step:2 - Install pythan depandancies
# pip install pyttsx3
# pip install PyPDF2

# Step:3 - Run Program
# D:\python-workspace>C:/Users/rgupta/AppData/Local/Programs/Python/Python310/python.exe d:/python-workspace/pdftoaudio.py

import pyttsx3
import PyPDF2

book = open('XXX.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

print(pages)

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
# alexa voice index
speaker.setProperty('voice', voices[1].id)
# speaking speed
speaker.setProperty('rate', 100)
speaker.say('I am your alexa')
speaker.runAndWait()

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

# with open('XXX.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)

#     # printing first page contents
#     pdf_page = pdf_reader.getPage(0)
#     print(pdf_page.extractText())

#     # reading all the pages content one by one
#     for page_num in range(pdf_reader.numPages):
#         pdf_page = pdf_reader.getPage(page_num)
#         print(pdf_page.extractText())
