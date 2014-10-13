# Created by Tasya Aditya Rukmana http://www.tadityar.web.id

# import pyPDF and easygui module
from pyPdf import PdfFileReader, PdfFileWriter
from easygui import *

# Choices to be generated in the buttonbox
choices = ("Open PDF File","Exit")
# Create a button box
command= buttonbox("Welcome to python PDF extractor!","Python PDF Extractor", choices)

if command == "Open PDF File":
	# Create a window to let user choose a file
	path = fileopenbox("Choose your file", "Open", "*.pdf")

	# Read the file
	input_file = PdfFileReader(file(path, "rb"))

	# Let user choose directory
	outpath = filesavebox("Where Do You Want To Save", "File")
	output_PDF = PdfFileWriter()

	# Get the page
	content = input_file.getPage(0)

	# Add the page
	output_PDF.addPage(content)

	# Create the output file
	output_file = file(outpath, "wb")

	# Write into it
	output_PDF.write(output_file)

	# Close the file
	output_file.close()
else:
	exit()