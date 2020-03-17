from csv import reader
from random import seed
from random import randrange
from math import sqrt

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
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

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
def cvs(dataset,folds):
    ds_split=list()
    ds_copy=list(dataset)
    fold_size=int(len(dataset)/folds)
    for i in range(folds):
        fold=list()
        while len(fold)<fold_size:
            index=randrange(len(ds_copy))
            fold.append(ds_copy.pop(index))
        ds_split.append(fold)
    return ds_split
def euc_dist(row1,row2):
    dist=0.0
    for i in range(len(row1)-1):
        dist+=(row1[i]-row2[i])**2
    return sqrt(dist)

def get_neighbours(train,test_row,num_neighbours):
    dist=list()
    for train_row in train:
        distance=euc_dist(train_row,test_row)
        dist.append((train_row,distance))
    dist.sort(key=lambda tup:tup[1])
    neighbours=list()
    for i in range(num_neighbours):
        neighbours.append(dist[i])
    return neighbours

def predict_classification(train,test_row,num_neighbours):
    neighbours=get_neighbours(train,test_row,num_neighbours)
    output_values=[row[-1] for row in neighbours]
    predict=max(set(output_values),key=output_values.count)
    return predict

def k_nearest_neighbours(train,test,num_neighbours=5):
        prediction=list()
        print("hi")
        for row in test:
                output=predict_classification(train,row,num_neighbours)
                prediction.append(output)
        return prediction    
            
def accuracy_metric(actual,predicted):
        correct=0.0
        for i in range(len(actual)):
                if actual[i]==predicted[i]:
                        correct+=1
        return correct/float(len(actual))*100.00

def evaluate_algo(dataset,algo,n_folds,*args):
    folds=cvs(dataset,n_folds)
    scores=list()
    for fold in folds:
        train_set=list(folds)
        train_set.remove(fold)
        train_set=sum(train_set,[])
        test_set=list()
        for row in fold:
            row_copy=list(row)
            test_set.append(row_copy)
            row_copy[-1]=None
        predicted=algo(train_set,test_set,*agrs)
        actual=[row[-1] for row in fold]
        print("MARK1")#""""eve_algo predict",predicted,"actual",actual""")
        accuracy=accuracy_metric(actual,predicted)
        scores.append(accuracy)
    return scores

seed(1)
filename = 'abalone.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
print('\n\n\n',dataset[0:5],'\n\n\n')
for i in range(1,len(dataset[0])):
	str_column_to_float(dataset, i)
print(dataset[0:5],"\n\n")
str_column_to_int(dataset, 0)
print(dataset[0:5],"\n\n")
"""# Calculate min and max for each column
minmax = dataset_minmax(dataset)
print(minmax)
# Normalize columns
normalize_dataset(dataset, minmax)
print(dataset[0:5][-1],'\n\n')"""
n_folds=5
num_neighbours=5
predict=evaluate_algo(dataset, k_nearest_neighbours,n_folds,num_neighbours)
print('scores:',predict)
