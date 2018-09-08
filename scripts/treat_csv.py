import shutil
import os
import csv
import glob

csv_treated_path = 'csv_treated'

def filter_csv():
	# create a copy of the csv folder
	shutil.copytree('csv_originals', csv_treated_path)

	# keep only the files with the list of accidents
	# we will filter for those by looking for "Natureza" in the header of the csv
	for file in os.listdir(csv_treated_path):
		#print(file)
		with open(os.path.join(csv_treated_path, file), newline='') as f:
			reader = csv.reader(f)
			row1 = next(reader)
		f.close()
		if "Natureza" not in row1:
			os.remove(os.path.join(csv_treated_path, file))

# merge the different csv files coming from different pages into a single csv per district
distritos = ['Aveiro', 'Beja', 'Bragança', 'Braga', 'Castelo Branco', 'Coimbra', 'Évora', 'Faro', 'Guarda', 'Leiria', 'Lisboa', 'Portalegre', 'Porto', 'Santarém', 'Setúbal', 'Viana do Castelo', 'Vila Real', 'Viseu']

def merge_csv(year):
	if not os.path.exists('csv_merge'):
		    os.makedirs('csv_merge')

	for distrito in distritos:
		allFiles = glob.glob(os.path.join(csv_treated_path, (distrito + " *.csv")))
		print(allFiles)
		with open(os.path.join('csv_merge', distrito + "_" + str(year) + ".csv"), 'wb') as outfile:
		    for i, fname in enumerate(allFiles):
		        with open(fname, 'rb') as infile:
		            if i != 0:
		                infile.readline()  # Throw away header on all but first file
		            # Block copy rest of file from input to output without parsing
		            shutil.copyfileobj(infile, outfile)
		            print(fname + " has been imported.")

filter_csv()
merge_csv(2015)