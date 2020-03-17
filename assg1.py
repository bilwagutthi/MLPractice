from csv import reader
from random import seed

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
def random_algo(train,test):
    output=[row[-1] for row in train]
    prediction=max(set(output),key=output.count)
    predicted=[prediction for i in range(len(test))]
    return predicted

filename = 'iris.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
print(dataset[0])
# convert string columns to float
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
print(dataset[0])
lookup = str_column_to_int(dataset, 4)
print(dataset[0])
seed(1)
train=dataset
test=[[None],[None],[None],[None]]
predictions=random_algo(train,test)
print(predictions)
