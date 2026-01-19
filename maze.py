import random
import copy

R=int(input())      #迷宮大小
C=int(input())
p=list()
for i in range(R):      #生成初始迷宮
    p.append(list())
    for j in range(C):
        p[i].append(random.choice([0,1]))
        if i>0 and j>0 and p[i][j]==0 and p[i-1][j]==0 and p[i][j-1]==0 and p[i-1][j-1]==0 :
            match random.randrange(1,5) :
                case 1 :
                    p[i][j]=1
                case 2 :
                    p[i-1][j]=1
                case 3 :
                    p[i][j-1]=1
                case 4 :
                    p[i-1][j-1]=1

rs=random.randrange(0,R)        #生成隨機開始點s及結束點e
cs=random.randrange(0,C)
re=random.randrange(0,R)
ce=random.randrange(0,C)
k=0
while abs(rs-re)+abs(cs-ce)<(R+C)/2 :
    re=random.randrange(0,R)
    ce=random.randrange(0,C)
    k+=1
    if k>100:
        break
'''rs=cs=0
re,ce=R-1,C-1
p[rs][cs]=p[re][ce]=0
'''
def count(a,b,item,maze):        #找出item方位
    lis=list()
    if a-1>=0 and maze[a-1][b]==item:
        lis.append(1)
    if b-1>=0 and maze[a][b-1]==item:
        lis.append(2)
    if a+1<R and maze[a+1][b]==item:
        lis.append(3)
    if b+1<C and maze[a][b+1]==item:
        lis.append(4)
    return lis

def countbomb(a,b,item,maze):        #找出炸開路徑方位
    lis=list()
    if a-1>=0 and p[a-1][b]==1 and len(count(a-1,b,item,maze))==1:
        lis.append(1)
    if b-1>=0 and p[a][b-1]==1 and len(count(a,b-1,item,maze))==1:
        lis.append(2)
    if a+1<R and p[a+1][b]==1 and len(count(a+1,b,item,maze))==1:
        lis.append(3)
    if b+1<C and p[a][b+1]==1 and len(count(a,b+1,item,maze))==1:
        lis.append(4)
    return lis

def add_d(a,b,maze,way,item,i):            #將沒有方向list的加入
    if len(way[i])==2:
        lis=list()
        if a-1>=0 and maze[a-1][b]!=1 and maze[a-1][b]<=item:
            lis.append(1)
        if b-1>=0 and maze[a][b-1]!=1 and maze[a][b-1]<=item:
            lis.append(2)
        if a+1<R and maze[a+1][b]!=1 and maze[a+1][b]<=item:
            lis.append(3)
        if b+1<C and maze[a][b+1]!=1 and maze[a][b+1]<=item:
            lis.append(4)
        way[i].append(lis)


allrc=list()
for a in range(R):
    for b in range(C):
        allrc.append([a,b])
mark=2

for nothing in range(R*C):
    r,c=random.choice(allrc)
    allrc.remove([r,c])
    if p[r][c]==0:
        way=[[r,c]]
        i=back=0
        while True:
            p[r][c]=mark
            add_d(r,c,p,way,mark-1,i)
            if len(way[i][2])==0:
                while len(way[i][2])==0:
                    if i==back:
                        bomb=random.randrange(0,len(way))
                        while len(countbomb(way[bomb][0],way[bomb][1],mark,p))==0:
                            del way[bomb]
                            if len(way)==0:
                                break
                            bomb=random.randrange(0,len(way))
                        if len(way)==0:
                            break
                        match random.choice(countbomb(way[bomb][0],way[bomb][1],mark,p)):
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
                        add_d(r,c,p,way,mark-1,i)
                        break
                    i-=1
                    r,c=way[i][0],way[i][1]
                if len(way)==0:
                    break
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
        mark+=1

for x in range(R):
    for y in range(C):
        if p[x][y]>1:
            p[x][y]=0

for row in p:
    print(*row)

"""(X)
p[rs][cs]='s'
p[re][ce]='e'
print("maze:")
for i in range(R):      #優化迷宮
    for j in range(C):
        if p[i][j]=='v':
            p[i][j]=0
        '''if i>0 and j>0 and p[i][j]==0 and p[i-1][j]==0 and p[i][j-1]==0 and p[i-1][j-1]==0 :
            turn1=list()
            if len(count(i,j,0,p))==2:
                turn1.append([i,j])
            if len(count(i-1,j,0,p))==2:
                turn1.append([i-1,j])
            if len(count(i,j-1,0,p))==2:
                turn1.append([i,j-1])
            if len(count(i-1,j-1,0,p))==2:
                turn1.append([i-1,j-1])
            if len(turn1)>=1:
                x=random.randrange(0,len(turn1))
                p[turn1[x][0]][turn1[x][1]]=1'''
    print(*p[i])

answer=copy.deepcopy(p)
answer[rs][cs]=answer[re][ce]=0
r,c=rs,cs
way=[[r,c]]
i=0
shortest=R*C
shortest_way=list()

while True :          #找出迷宮最短的解答
    answer[r][c]=2
    add_d(r,c,answer,way,0,i)
    if len(way[i][2])==0:
        while len(way[i][2])==0:
            answer[r][c]=0
            way.pop()
            i-=1
            if i<0:
                break
            r,c=way[i][0],way[i][1]
        if i<0:
            break
        continue
    match way[i][2].pop():
        case 1:
            r-=1
        case 2:
            c-=1
        case 3:
            r+=1
        case 4:
            c+=1
    if r==re and c==ce:
        if len(way)<shortest:
            shortest=len(way)
            shortest_way=copy.deepcopy(way)
        continue
    i+=1
    way.insert(i,[r,c])

answer[rs][cs]='s'
answer[re][ce]='e'
print("answer:")
for rc in shortest_way[1:]:
    answer[rc[0]][rc[1]]='v'
for row in answer :
    print(*row)
print(shortest)
"""
