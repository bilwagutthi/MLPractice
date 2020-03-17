from math import sqrt

def euc_dist(row1,row2):
    dist=0.0
    for i in range(len(row1)-1):
        dist+=(row1[i]-row2[i])**2
    return sqrt(dist)

def get_neighbours(train,test_row,num_neighbours):
    dist=list()
    for train_row in train:
        distance=euc_dist(train_row,test_row)
        dist.append((train_row,distance))
    dist.sort(key=lambda tup:tup[1])
    neighbours=list()
    for i in range(num_neighbours):
        neighbours.append(dist[i])
    print(neighbours)
    return neighbours

def predict_classification(train,test_row,num_neighbours):
    neighbours=get_neighbours(train,test_row,num_neighbours)
    output_values=[row[-1] for row in neighbours]
    predict=max(set(output_values),key=output_values.count)
    return predict

dataset=[[2.781,2.55,0],
         [1.465,2.36,0],
         [3.396,4.400,0],
         [1.388,1.850,-0],
         [3.064,3.0,0],
         ]
row0=dataset[0]
for row in dataset:
    dist=euc_dist(row0,row)
    print(dist)

predicted=predict_classification(dataset,dataset[0],3)
print("Expected %d , Got %d"%(dataset[0][-1],predicted))
