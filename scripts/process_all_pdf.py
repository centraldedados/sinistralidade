from get_list_accidents import get_list_accidents
import os

# create folder to store data in csv
path_csv = os.path.join("..", "dados")
if not os.path.exists(path_csv):
    os.makedirs(path_csv)

# list districts
distritos = [
    "Aveiro",
    "Beja",
    "Braga",
    "Bragança",
    "Castelo",
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
    "Viana",
    "Vila",
    "Viseu",
]

# define function to process all the districts in a given year
def process_all_pdfs_in_folder(year):

    print("Processing year", year)

    path_pdfs = os.path.join("..", "pdfs", str(year))

    # get list of all pdf files inside the folder
    list_pdfs = [f for f in os.listdir(path_pdfs) if f.endswith(".pdf")]

    print("List of pdf files in the folder:", list_pdfs)

    # keep only the pdfs that start with a district name
    final_list = [
        item for item in list_pdfs for distrito in distritos if distrito in item
    ]
    final_list = list(
        sorted(set(final_list))
    )  # drops duplicates from the list, caused by Braga and Bragança

    print("Final list of files:", final_list)

    # for each file, extract the list of accidents and move it to the data folder
    for file in final_list:

        print("Processing file", file)

        # convert list of accidents to csv
        path_pdf_file = os.path.join(path_pdfs, file)
        get_list_accidents(path_pdf_file)
        csv_filename = os.path.splitext(file.replace(" ", "_"))[0] + ".csv"

        # move the file
        os.rename(
            os.path.join(path_pdfs, csv_filename), os.path.join(path_csv, csv_filename)
        )


# loop through all the years in the data
for year in range(2017, 2003, -1):
    print("Processing year", year)
    process_all_pdfs_in_folder(year)
