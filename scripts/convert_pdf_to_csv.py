# This file uses tabula-py to convert each page in the pdfs to a csv table
# Leave original pdf files inside a "pdfs" directory

import tabula
import PyPDF2
import os

def get_num_pages_pdf(file):
	pdfFileObj = open(file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	return pdfReader.numPages

def main():
	path_pdfs = 'pdfs'
	path_csv_originals = 'csv_originals'

	# create folder to store csv files
	if not os.path.exists(path_csv_originals):
	    os.makedirs(path_csv_originals)

	# get list of pdf files
	list_pdfs = [f for f in os.listdir(path_pdfs) if f.endswith('.pdf')]

	# in each file, loop through each page and convert the table inside to a pdf
	for file in list_pdfs:
		path_file = os.path.join(path_pdfs,file)

		for page in range(1,get_num_pages_pdf(path_file)+1):
			print(page)
			csv_filename = str(file) + '_p' + str(page) + '.csv'
			tabula.convert_into(path_file,  os.path.join(path_csv_originals,csv_filename), output_format="csv", encoding='latin-1', pages=page, multiple_tables = True, lattice = True)

main()