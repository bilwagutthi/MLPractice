from math import sqrt

def euc_dist(row1,row2):
    dist=0.0
    for i in range(len(row1)-1):
        dist+=(row1[i]-row2[i])**2
    return sqrt(dist)

dataset=[[6.0, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50.0, 1.0], [1.0, 85.0, 66.0, 29.0, 0.0, 26.6, 0.351, 31.0, 0.0], [8.0, 183.0, 64.0, 0.0, 0.0, 23.3, 0.672, 32.0, 1.0], [1.0, 89.0, 66.0, 23.0, 94.0, 28.1, 0.167, 21.0, 0.0], [0.0, 137.0, 40.0, 35.0, 168.0, 43.1, 2.288, 33.0, 1.0]]
row0=dataset[0]
for row in dataset:
    dist=euc_dist(row0,row)
    print(dist)
