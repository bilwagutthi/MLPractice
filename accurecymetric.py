def am(acc,pre):
    correct=0
    for i in range(len(acc)):
        if acc[i]==pre[i]: correct+=1
    return correct/float(len(acc))*100.0
actual=[0,0,0,0,0,1,1,1,1,1]
pre=[0,1,0,0,0,1,0,1,1,1]
acc=am(actual,pre)
print(acc)