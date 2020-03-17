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

def train_test(ds,split=0.60):
    train=list()
    data_copy=list(ds)
    train_size=split*len(ds)
    while len(train)<train_size:
        index=randrange(len(data_copy))
        train.append(data_copy.pop(index))
    return train,data_copy

#co-eff calculation
def mean(value):
    return sum(value)/float(len(value))
def covar(x,mx,y,my):
    cov=0
    for i in range(len(x)):
        cov+=(x[i]-mx)*(y[i]-my)
    return cov
def var(values,mean):
    return sum([(x-mean)**2 for x in values])
def coeff(dataset):
    x=[row[0] for row in dataset]
    y=[row[1] for row in dataset]
    xm,ym=mean(x),mean(y)
    b1=covar(x,xm,y,ym)/var(x,xm)
    b0=ym-b1*xm
    return [b0,b1]

def evaluate_algo(dataset,algo,b0,b1):
    ts=list()
    for row in dataset:
        rc=list(row)
        rc[-1]=None
        ts.append(rc)
    predicted=algo(ts,b0,b1)
    print('\n\nPredicted values :',predicted)
    actual=[row[-1] for row in dataset]
    rmse=rmse_metric(actual,predicted)
    return rmse

def simple_liner_reg(test,b0,b1):
    predictions=list()
    for row in test:
        yhat=b0+b1*row[0]
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
filename = 'insurance.csv'
dataset = load_csv(filename)
#Convert from string to float
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
#Make Train and Test set
seed(1)
ds=dataset
train,test=train_test(ds)
print('\n\nTrain set:',train)
print('\n\nTest set:',test)
#Calculate co-efficients for train set
b0,b1=coeff(train)
print("coefficients: b0=3%f, b1=%3f"%(b0,b1))
#Prediction and rmse calculation
tt=test
rmse=evaluate_algo(tt,simple_liner_reg,b0,b1)
print("\n\nrmse:%3f"%(rmse))

