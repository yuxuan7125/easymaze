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
                #turn1=random.randrange(1,5)
                match random.randrange(1,5) :
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
p[rs][cs]=p[re][ce]=0
r,c=rs,cs
def count(a,b,item):        #找出item方位
    lis=list()
    if a-1>=0 and p[a-1][b]==item:
        lis.append(1)
    if b-1>=0 and p[a][b-1]==item:
        lis.append(2)
    if a+1<R and p[a+1][b]==item:
        lis.append(3)
    if b+1<C and p[a][b+1]==item:
        lis.append(4)
    return lis
def countbomb(a,b):        #找出炸開路徑方位
    lis=list()
    if a-1>=0 and p[a-1][b]==1 and len(count(a-1,b,2))<=1:
        lis.append(1)
    if b-1>=0 and p[a][b-1]==1 and len(count(a,b-1,2))<=1:
        lis.append(2)
    if a+1<R and p[a+1][b]==1 and len(count(a+1,b,2))<=1:
        lis.append(3)
    if b+1<C and p[a][b+1]==1 and len(count(a,b+1,2))<=1:
        lis.append(4)
    return lis
way=[[r,c]]
i=back=0
p[re][ce]=3
while r!=re or c!=ce :
    p[r][c]=2
    if len(way[i])==2:
        way[i].append(count(way[i][0],way[i][1],0))
    if len(way[i][2])==0:
        while len(way[i][2])==0:
            if i==back:         #開路
                bomb=random.randrange(0,len(way))
                while len(countbomb(way[bomb][0],way[bomb][1]))==0:
                    bomb=random.randrange(0,len(way))
                match random.choice(countbomb(way[bomb][0],way[bomb][1])):
                    case 1:
                        r,c=way[bomb][0]-1,way[bomb][1]
                    case 2:
                        r,c=way[bomb][0],way[bomb][1]-1
                    case 3:
                        r,c=way[bomb][0]+1,way[bomb][1]
                    case 4:
                        r,c=way[bomb][0],way[bomb][1]+1
                p[r][c]=0
                way.append([r,c])
                i=len(way)-1
                back=i
                break
            i-=1
            r,c=way[i][0],way[i][1]
        continue
    d=random.choice(way[i][2])
    way[i][2].remove(d)
    match d:
        case 1:
            r-=1
        case 2:
            c-=1
        case 3:
            r+=1
        case 4:
            c+=1
    i+=1
    way.insert(i,[r,c])
for row in p :
    print(*row)
