import os
import shutil
import re
import fileinput
import csv

original_csv_path = os.path.join("..", "dados")
treated_csv_path = os.path.join("..", "dados_treated")

if os.path.isdir(treated_csv_path):
    shutil.rmtree(treated_csv_path)

shutil.copytree(original_csv_path, treated_csv_path)


def emptycols(file):
    with open(file, newline="") as f:
        reader = csv.reader(f)
        try:
            row1 = next(reader)
        except StopIteration:
            row1 = ""
    return [idx for idx, item in enumerate(row1) if item == ""]


def fix_empty_columns(input_file):
    csv_filename = os.path.join(treated_csv_path, input_file)
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


def treat_csv(input_file):
    with open(os.path.join(treated_csv_path, input_file), "r") as f:
        content = f.read()

    # Fix empty header lines in files from 2007 and earlier
    # remove lines starting with "" and then any number of commas
    # content = re.sub(r'^""(,)+\n', '', content, flags = re.M)
    # lines without any alphanumeric
    content = re.sub(r"^[^\d\w]+\n", r"", content, flags=re.M)
    content = re.sub(r"^11. Listagem.*\n", r"", content, flags=re.M)

    # Fix column names
    content = re.sub(r"Datahora,M\*,FG\*", r"Datahora,M,FG", content, flags=re.M)

    # remove lines which have the sums at the bottom of the table, imported
    content = re.sub(r'^""(,)+[0-9]+(,)+[0-9]+(,)+\n', r"", content, flags=re.M)

    # single commas at the end of the line
    content = re.sub(r"[^,],$", r"", content, flags=re.M)

    # cases where first two columns got separated
    # content = re.sub(r'^[A-z]+,,', '^[A-z]+,', content, flags = re.M)

    with open(os.path.join(treated_csv_path, input_file), "w") as f:
        f.write(content)


list_csvs = [f for f in os.listdir(treated_csv_path) if f.endswith(".csv")]

for file in list_csvs:

    # get the year with regex
    year = re.findall("([0-9]{4})", file)[0]

    if int(year) > 2007:
        fix_empty_columns(file)

    treat_csv(file)

    # fix line breaks inside values
    print(file)
    with open(
        os.path.join(treated_csv_path, file), "r", encoding="ISO-8859-1"
    ) as input:
        reader = csv.reader(input)
        new_file = []
        for row in reader:
            row = [el.replace("\n", " ") for el in row]
            new_file.append(row)

    with open(
        os.path.join(treated_csv_path, file), "w", encoding="utf-8", newline=""
    ) as output:
        writer = csv.writer(output)
        writer.writerows(new_file)
