def mean_metric(actual,predicted):
	sumerr=0
	for i in range(len(actual)):
		sumerr+=abs(actual[i]-predicted[i])
	return sumerr/float(len(actual))

actual=[0.1,0.2,0.3,0.4,0.5]
predicted=[0.11,0.19,0.29,0.41,0.5]
mae=mean_metric(actual,predicted)
print(mae)
