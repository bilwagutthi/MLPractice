from random import seed
from random import randrange
def random_algo(train,test):
    output=[row[-1] for row in train]
    prediction=max(set(output),key=output.count)
    predicted=[prediction for i in range(len(test))]
    return predicted
seed(1)
train=[[1,0],[2,10],[2,0],[5,1],[0,3],[10,20]]
test=[[None],[None],[None],[None]]
predictions=random_algo(train,test)
print(predictions)

