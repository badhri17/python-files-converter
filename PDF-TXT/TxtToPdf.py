#by badhri17
from fpdf import FPDF

def text_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write(5, text)
    pdf.output(filename, "F")

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
lor sit amet, consectetur adipiscing elit.
lor sit amet, consectetur adipiscing elit.
lor sit amet, consectetur adipiscing elit.
lor sit amet, consectetur adipiscing elit.
lor sit amet, consectetur adipiscing elit.

"""                                                         

# or load from file

# with open("yourpath", "r") as f:
#     text = f.read()

text_to_pdf(text, r"path\output.pdf")