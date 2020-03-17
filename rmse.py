from math import sqrt

def rmse_metric(actual,predicted):
	sumerr=0
	for i in range(len(actual)):
		prederr=abs(actual[i]-predicted[i])
		sumerr+=prederr**2
	mean_err=sumerr/float(len(actual))
	return sqrt(mean_err)

actual=[0.1,0.2,0.3,0.4,0.5]
predicted=[0.11,0.19,0.29,0.41,0.5]
rmse=rmse_metric(actual,predicted)
print(rmse)
