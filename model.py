def parseDate(s):
    l=s.split('-')
    adict={}
    adict['year']=l[0]
    adict['month']=l[1]
    adict['day']=l[2]
    return adict

def calcLoss(act,pred):
    return (act-pred)**2

def calcError(act,pred):
    return act-pred
    
def avg(l):
    acc=0
    num=0
    for i in l:
        acc+=i
        num+=1
    return acc/num

def dotProd(l1,l2):
    acc=0
    if len(l1)!=len(l2):
        raise IndexError
    for i in range(0,len(l1)):
        acc+=l1[i]*l2[i]
    return acc

def norm(l):
    M=[]
    m=[]
    for i in range(0,len(l[0])):
        M.append(l[0][i])
        m.append(l[0][i])
    for i in range(0,len(l[0])):
        for j in range(0,len(l)):
            if l[j][i]<m[i]:
                m[i]=l[j][i]
            elif l[j][i]>M[i]:
                M[i]=l[j][i]
    for i in range(0,len(l[0])):
        for j in range(0,len(l)):
            l[j][i]=(l[j][i]-m[i])/(M[i]-m[i])
    list1=[]
    list1.append(M)
    list1.append(m)
    return list1
def norm1(l):
    sum1=[]
    for i in range(0,len(l[0])):
        sum1.append(l[0][i])
        sum1.append(l[0][i])
    for i in range(0,len(l[0])):
        for j in range(0,len(l)):
            sum1[i]+=l[j][i]
    for i in range(0,len(l[0])):
        for j in range(0,len(l)):
            l[j][i]-=sum1[i]
def denorm(l1,index,val):
    Mi=l1[0][index]
    mi=l1[1][index]
    return val*(Mi-mi)+mi
def train(alpha):
    corr=[0,0,0,0,0,0]
    for i in range(0,len(rows)-1):
        act=rows[i+1][1]
        data=rows[i].copy()
        data.insert(0,1)
        pred=dotProd(trainVec,data)
        for i in range(0,len(corr)):
            corr[i]+=calcError(act,pred)*data[i]
    for i in range(0,len(corr)):
        corr[i]/=(len(rows))
    for i in range(0,len(corr)):
        trainVec[i]+=2*alpha*corr[i]

import csv
rows=[]

with open("ADD FILEPATH", 'r', newline='') as csvfile:
    rd=csv.reader(csvfile,delimiter=",")
    for row in rd:
        if row[0]=='date':
            continue
        if row[1]=='AAPL':
            data=[float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6])]
            rows.append(data)
list1=norm(rows)
trainVec=[0,0,0,0,0,0]
def test():
    loss=0
    for i in range(0,len(rows)-1):
        data=rows[i].copy()
        data.insert(0,1.0)
        pred=dotProd(trainVec,data)
        print(denorm(list1,1,rows[i+1][1]),denorm(list1,1,pred))
        loss+=calcLoss(denorm(list1,1,rows[i+1][1]),denorm(list1,1,pred))
    loss/=(len(rows)-1)
    print(loss)    
def main():
    for epoch in range(1,21):
        alpha=0.1/epoch
        for i in range(0,100):
            train(alpha)
    test()
        
main()         
print(trainVec)
