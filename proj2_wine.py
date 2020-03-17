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

#cross vald

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

def train_test(ds,split=0.60):
    train=list()
    data_copy=list(ds)
    train_size=split*len(ds)
    while len(train)<train_size:
        index=randrange(len(data_copy))
        train.append(data_copy.pop(index))
    return train,data_copy

def predict(row,coeff):
    yhat=coeff[0]
    for i in range(len(row)-1):
        yhat+=coeff[i+1]*row[i]
    return yhat

def coeff_sgd(train,l_rate,n_epoch):
    coef=[0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sumerror=0
        for row in train:
            yhat=predict(row,coef)
            error=yhat-row[-1]
            sumerror+=error**2
            coef[0]=coef[0]-l_rate*error
            for i in range(len(row)-1):
                coef[i+1]=coef[i+1]-l_rate*error*row[i]
        #print('epoch=%d,lrate=%.3f,error=%.3f'%(epoch,l_rate,sumerror))
    return coef

def evaluate_algo(dataset,algo,n_folds):
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
        predicted=algo(train_set,test_set)
        actual=[row[-1] for row in fold]
        rmse=rmse_metric(actual,predicted)
        scores.append(rmse)
    return scores

def liner_reg_sgd(train,test):
    l_rate=0.01
    n_epoch=50
    predictions=list()
    coef=coeff_sgd(train,l_rate,n_epoch)
    for row in test:
        yhat=predict(row,coef)
        predictions.append(yhat)
    return predictions

def rmse_metric(actual,predicted):
    sum_err=0.0
    for i in range(len(actual)):
        prederr=predicted[i]-actual[i]
        sum_err+=(prederr**2)
    meanerr=sum_err/float(len(actual))
    return sqrt(meanerr)

# Load dataset
seed(1)
filename = 'winequality-white.csv'
dataset = load_csv(filename)
#Convert from string to float
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
# Calculate min and max for each column
minmax = dataset_minmax(dataset)
print("\nRow | Min\tMax ")
count=1
for i in minmax:
        print("{0} | {1:.3f}   {2:.3f}".format(count,i[0],i[1]))
        count+=1
# Normalize columns
normalize_dataset(dataset, minmax)
n_folds=5
scores=evaluate_algo(dataset,liner_reg_sgd,n_folds)
print("\n\nrmse:%s"%(scores))
print("\n Mean: %.3f"%(sum(scores)/float(len(scores))))

