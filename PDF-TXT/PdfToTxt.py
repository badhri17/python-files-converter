# python simple script to convert pdf to text by badhri17
import fitz  # pip install pymupdf

def convertPdfToText(path):
    with fitz.open(path) as doc:
        text = ""
        for page in doc:
            text += page.getText()

    return(text)



text = convertPdfToText(r"C:\Users\badrb\Documents\projects\python-files-converter\PDF-TXT\sample.pdf")  # put your file path 
print(text) 
# if you want to save your text in txt file
with open(r"C:\Users\badrb\Documents\projects\python-files-converter\PDF-TXT\output.txt", "w") as text_file: 
    text_file.write(text)  
