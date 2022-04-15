#by badhri17 
import img2pdf,os

#os.chdir(r"")

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert('sample.jpg'))