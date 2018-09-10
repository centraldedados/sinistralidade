# This scripts renames the csv files created after processing all the pdfs
# The pdfs are named inconsistently, which leads to inconsistent names for the csv
# This file solves this
import os
import re

# create folder to store data in csv
path_csv = os.path.join("..", "dados")

# districts short and long names in a dict
# using the first word of a district name as a short name so _ can be used to split strings
distritos_long_name = [
    "Aveiro",
    "Beja",
    "Braga",
    "Bragança",
    "Castelo Branco",
    "Coimbra",
    "Évora",
    "Faro",
    "Guarda",
    "Leiria",
    "Lisboa",
    "Portalegre",
    "Porto",
    "Santarém",
    "Setúbal",
    "Viana do Castelo",
    "Vila Real",
    "Viseu",
]
distritos_short_name = [distrito.split()[0] for distrito in distritos_long_name]
districtos_zip = zip(distritos_short_name, distritos_long_name)
distritos_dict = {}
for short_name, long_name in districtos_zip:
    distritos_dict[short_name] = long_name

# get all files
list_files = [f for f in os.listdir(path_csv)]

# rename each file
for filename in list_files:

    # get short name from the first part of the file name
    short_name = filename.split("_")[0]

    # handle potential errors when districts have multiple names
    if short_name.startswith("Viana"):
        short_name = "Viana"
    if short_name.startswith("Castelo"):
        short_name = "Castelo"
    if short_name.startswith("Vila"):
        short_name = "Vila"

    # get the long name from the dictionary we created
    long_name = distritos_dict[short_name]

    # get the year with regex
    year = re.findall("([0-9]{4})", filename)

    # make sure only 1 year was caught:
    assert len(year) == 1
    year = year[0]

    # get whether 24 hours or 30 days
    check30 = re.findall("(30)", filename)

    if check30:
        horizon = "30d"
    else:
        horizon = "24h"

    # rename the file
    final_filename = long_name.replace(" ", "") + "_" + year + "_" + horizon + ".csv"
    print(final_filename)
    os.rename(os.path.join(path_csv, filename), os.path.join(path_csv, final_filename))
