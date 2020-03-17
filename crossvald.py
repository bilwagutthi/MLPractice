from random import seed
from random import randrange

def cvs(dataset,folds):
    ds_split=list()
    ds_copy=list(dataset)
    fold_size=int(len(dataset)/folds)
    for i in range(folds):
        fold=list()
        while len(fold)<fold_size:
            index=randrange(len(ds_copy))
            fold.append(ds_copy.pop(index))
        ds_split.append(fold)
    return ds_split

seed(1)
ds=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
folds=cvs(ds,3)
print(folds)