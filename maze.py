import random

R=int(input())      #迷宮大小
C=int(input())
p=list()
for i in range(R):      #生成初始迷宮
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
                        p[i-1][j-1]=1
rs=random.randrange(0,R)        #生成開始點s及結束點e
cs=random.randrange(0,C)
re=random.randrange(0,R)
ce=random.randrange(0,C)
while rs==re and cs==ce:
    re=random.randrange(0,R)
    ce=random.randrange(0,C)
r,c=rs,cs
way=[[r,c]]
def countd(a,b):        #找出空白0方位
    lis=list()
    if a-1>=0 and p[a-1][b]==0:
        lis.append(1)
    if b-1>=0 and p[a][b-1]==0:
        lis.append(2)
    if a+1<R and p[a+1][b]==0:
        lis.append(3)
    if b+1<C and p[a][b+1]==0:
        lis.append(4)
    return lis
alld=countd(r,c)
if len(alld)==0 :       #避免開始點s四周皆為牆1
    while True:
        w=random.randrange(1,5)
        if w==1 and r-1>=0:
            p[r-1][c]=1
            break
        if w==2 and c-1>=0:
            p[r-1][c]=1
            break
        if w==3 and r+1<R:
            p[r-1][c]=1
            break
        if w==4 and c+1<C:
            p[r-1][c]=1
            break       
i=0
while r!=re and c!=ce :
    alld=countd(way[i][0],way[i][1])
    d=random.choice(alld)
    alld.remove(d)
    
for row in p :
    print(*row)
