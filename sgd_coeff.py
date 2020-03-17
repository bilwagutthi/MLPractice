from math import sqrt

def rmse_metric(actual,predicted):
	sumerr=0
	for i in range(len(actual)):
		prederr=abs(actual[i]-predicted[i])
		sumerr+=prederr**2
	mean_err=sumerr/float(len(actual))
	return sqrt(mean_err)

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
        print('epoch=%d,lrate=%.3f,error=%.3f'%(epoch,l_rate,sumerror))
    return coef

dataset=[[1,1],[2,3],[4,3],[3,2],[5,5]]
l_rate=0.001
n_epoch=50
co_ef=coeff_sgd(dataset,l_rate,n_epoch)
print('co-eff',co_ef)
predicted=[predict(row,co_ef) for row in dataset]
actual=[row[-1] for row in dataset]
rmse=rmse_metric(actual,predicted)
print('Predicted',predicted)
print('Actual',actual)
print('rmse',rmse)
