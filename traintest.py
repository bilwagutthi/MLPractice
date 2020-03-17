from random import seed
from random import randrange

def train_test(ds,split=0.60):
    train=list()
    data_copy=list(ds)
    train_size=split*len(ds)
    while len(train)<train_size:
        index=randrange(len(data_copy))
        train.append(data_copy.pop(index))
    return train,data_copy

seed(1)
ds=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
train,test=train_test(ds)
print(train,test)