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

dataset=[[1,1],[2,3],[4,3],[3,2],[5,5]]
b0,b1=coeff(dataset)
print("coefficients: b0=3%f, b1=%3f"%(b0,b1))
