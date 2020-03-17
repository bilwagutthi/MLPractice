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


def accuracy_metrix(actual,predicted):
    correct=0
    for i in range(len(actual)):
        if(predicted[i] in range(1,6)):predicted[i]=0
        elif(predicted[i] in range(6,15)):predicted[i]=1
        else:predicted[i]=2
        if(actual[i] in range(1,6)):actual[i]=0
        elif(actual[i] in range(6,15)):actual[i]=1
        else:actual[i]=2
        if actual[i]==predicted[i]:correct+=1
    return correct / float(len(actual)) * 100.0

def evaluate_algorithm(dataset,algorithm,n_folds, *args):
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
        predicted=algorithm(train_set,test_set, *args)
        actual=[row[-1] for row in fold]
        print("mark1")
        accuracy=accuracy_metrix(actual,predicted)
        scores.append(accuracy)
    return scores





def euclidean_distance(row1,row2):
    distance=0.0
    for i in range(len(row1)-1):
        distance+=(row1[i]-row2[i])**2
    return sqrt(distance)

def get_neighbors(train,test_row,num_neighbors):
    distances=list()
    for train_row in train:
        dist=euclidean_distance(test_row,train_row)
        distances.append((train_row,dist))
    distances.sort(key=lambda tup:tup[1])
    neighbors=list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


def predict_classification(train,test_row,num_neighbors):
    neighbors=get_neighbors(train,test_row,num_neighbors)
    output_values=[row[-1] for row in neighbors]
    prediction=max(set(output_values),key=output_values.count)
    return prediction

    
def k_nearest_neighbors(train,test,num_neughbors):
    predictions=list()
    for row in test:
        output=predict_classification(train,row,num_neighbors)
        predictions.append(output)
    return(predictions)




seed(1)
filename ='abalone.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
print('\n\n\n',dataset[0:5],'\n\n\n')
for i in range(1,len(dataset[0])):
	str_column_to_float(dataset, i)
str_column_to_int(dataset,0)
n_folds=5
num_neighbors=5
scores=evaluate_algorithm(dataset,k_nearest_neighbors,n_folds,num_neighbors)
print('scores:%s'%scores)
print('mean accuracy:%.3f%%'%(sum(scores)/float(len(scores))))



