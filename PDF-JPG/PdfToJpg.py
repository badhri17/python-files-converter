# python program to convert PDF to JPG by badhri17
# requires pdf2image and poppler
from pdf2image import convert_from_path
import os

#os.chdir()
filename = r"sample.pdf"  # directory and name of the file

#install poppler https://github.com/oschwartz10612/poppler-windows/releases/
pages = convert_from_path(filename, 500, poppler_path = r'Release-22.01.0-0\poppler-22.01.0\Library\bin') #path to poppler
for i in range(len(pages)): # loop page by page
    pages[i].save(r'{}.jpg'.format(i), 'JPEG') #where to save the page

