# This file uses tabula-py to convert the list of accidents in the pdf reports to a csv table
import tabula
import PyPDF2
import os
import sys
import shutil
import csv
import glob
import re


def get_year_from_filename(filename):
    year = re.findall("([0-9]{4})", filename)
    return year[-1]


def get_num_pages_pdf(file):
    pdfFileObj = open(file, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    return pdfReader.numPages


def convert_pdfs(pdf_input):

    # 2012 seems to require this option to be turned off to get good results
    lattice_toggle = True
    if get_year_from_filename(pdf_input) == "2012":
        lattice_toggle = False

    for page in range(1, get_num_pages_pdf(pdf_input) + 1):
        print(page)
        csv_filename = str(pdf_input) + "_p" + str(page) + ".csv"
        tabula.convert_into(
            pdf_input,
            csv_filename,
            output_format="csv",
            encoding="latin-1",
            pages=page,
            lattice=lattice_toggle,
        )


def filter_csv(pdf_input):
    # keep only the files with the list of accidents
    # we will filter for those by looking for "Natureza" in the header of the csv
    for file in glob.glob(pdf_input + "_p*.csv"):
        print(file)
        # print(file)
        with open(file, newline="") as f:
            reader = csv.reader(f)
            try:
                row1 = next(reader)
            except StopIteration:
                row1 = ""
        f.close()
        if "Natureza" not in row1:
            os.remove(file)


def merge_csv(pdf_input):
    allFiles = glob.glob(pdf_input + "_p*.csv")
    print(allFiles)
    with open(os.path.join(pdf_input + ".csv"), "wb") as outfile:
        for i, fname in enumerate(allFiles):
            with open(fname, "rb") as infile:
                if i != 0:
                    infile.readline()  # Throw away header on all but first file
                # Block copy rest of file from input to output without parsing
                shutil.copyfileobj(infile, outfile)
                print(fname + " has been imported.")
    os.rename(
        pdf_input + ".csv", os.path.splitext(pdf_input.replace(" ", "_"))[0] + ".csv"
    )
    for file in allFiles:
        os.remove(file)


def emptycols(file):

    with open(file, newline="") as f:
        reader = csv.reader(f)
        try:
            row1 = next(reader)
        except StopIteration:
            row1 = ""

    return [idx for idx, item in enumerate(row1) if item == ""]


def fix_empty_columns(pdf_input):
    csv_filename = os.path.splitext(pdf_input.replace(" ", "_"))[0] + ".csv"

    # fix empty column headers when converting some files
    # ex: "",Concelho,Datahora,M,FG,,Via,Km,Natureza
    # Get index of columns with empty header to be merged
    # Merge columns recursively when empty
    while emptycols(csv_filename):

        emptycoltomerge = emptycols(csv_filename)[0]

        temp_filename = csv_filename + "_temp"
        os.rename(csv_filename, temp_filename)

        with open(temp_filename) as f:
            reader = csv.reader(f)
            with open(csv_filename, "w", newline="") as g:
                writer = csv.writer(g)
                for row in reader:
                    try:
                        new_row = (
                            row[0:emptycoltomerge]
                            + [
                                "".join(
                                    [row[emptycoltomerge], row[emptycoltomerge + 1]]
                                )
                            ]
                            + row[emptycoltomerge + 2 :]
                        )
                    # some rows are missing a last empty column in these files
                    except IndexError:
                        new_row = row[0:emptycoltomerge]
                    writer.writerow(new_row)
        os.remove(temp_filename)


def get_list_accidents(pdf_input):
    convert_pdfs(pdf_input)
    filter_csv(pdf_input)
    merge_csv(pdf_input)
    fix_empty_columns(pdf_input)


## Uncomment these to call this function from a command line
# assert len(sys.argv[1:]) == 1, "Only one argument allowed: the path to the pdf"
# pdf_filename = str(sys.argv[1])
# get_list_accidents(pdf_filename)
