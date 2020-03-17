from random import seed
from random import randrange
def zero_reg_algo(train,test):
    output=[row[-1] for row in train]
    prediction=sum(output)/float(len(output))
    predicted=[prediction for i in range(len(test))]
    return predicted

seed(1)
train=[[10],[15],[12],[15],[18],[20]]
test=[[None],[None],[None],[None]]
predictions=zero_reg_algo(train,test)
print(predictions)
