from math import sqrt

def rmse_metric(actual,predicted):
    sum_err=0.0
    for i in range(len(actual)):
        prederr=predicted[i]-actual[i]
        sum_err+=(prederr**2)
    meanerr=sum_err/float(len(actual))
    return sqrt(meanerr)

def evaluate_algo(dataset,algo):
    ts=list()
    for row in dataset:
        rc=list(row)
        rc[-1]=None
        ts.append(rc)
    predicted=algo(dataset,ts)
    print(predicted)
    actual=[row[-1] for row in dataset]
    rmse=rmse_metric(actual,predicted)
    return rmse

def mean(value):
    return sum(value)/float(len(value))
def covar(x,mx,y,my):
    cov=0.0
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

def simple_liner_reg(train,test):
    predictions=list()
    b0,b1=coeff(train)
    for row in test:
        yhat=b0+b1*row[0]
        predictions.append(yhat)
    return predictions

dataset=[[1,1],[2,3],[4,3],[3,2],[5,5]]
b0,b1=coeff(dataset)
print("coefficients: b0=3%f, b1=%3f"%(b0,b1))
rmse=evaluate_algo(dataset,simple_liner_reg)
print("rmse:%3f"%(rmse))
