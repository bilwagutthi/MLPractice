from random import seed
from random import randrange
def random_algo(train,test):
    output=[row[-1] for row in train]
    unique=list(set(output))
    predicted=list()
    for i in test:
        index=randrange(len(unique))
        predicted.append(unique[index])
    return predicted

seed(1)
train=[[1,0],[2,10],[2,0],[5,1],[0,3],[10,20]]
test=[[None],[None],[None],[None]]
predictions=random_algo(train,test)
print(predictions)
