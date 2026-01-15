import random

R=int(input())
C=int(input())  #迷宮大小
p=list()
for i in range(R):
    p.append(list())
    for j in range(C):
        p[i].append(random.choice([0,1]))
        if i>0 and j>0 :
            if p[i][j]==0 and p[i-1][j]==0 and p[i][j-1]==0 and p[i-1][j-1]==0 :
                turn1=random.randrange(1,5)
                match turn1 :
                    case 1 :
                        p[i][j]=1
                    case 2 :
                        p[i-1][j]=1
                    case 3 :
                        p[i][j-1]=1
                    case 4 :
                        p[i-1][j-1]=1   #生成初始迷宮
rs=random.randrange(0,R)
cs=random.randrange(0,C)
re=random.randrange(0,R)
ce=random.randrange(0,C)
while rs==re and cs==ce:
    re=random.randrange(0,R)
    ce=random.randrange(0,C)    #生成開始點s及結束點e
for row in p :
    print(*row)
