import csv

def parse_csv(path):
	output = []
	with open(path, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_NONE, skipinitialspace=True)
		for row in reader:
			output.append(row)
	return output

def save_duration_matrix(duration_matrix, output_path):
	writer = csv.writer(open(output_path, 'w'), delimiter=';', quoting=csv.QUOTE_MINIMAL)
	for row in duration_matrix:
		writer.writerow(row)

