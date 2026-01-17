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

'''rs=random.randrange(0,R)        #生成隨機開始點s及結束點e
cs=random.randrange(0,C)
re=random.randrange(0,R)
ce=random.randrange(0,C)
k=0
while abs(rs-re)+abs(cs-ce)<(R+C)/2 :
    re=random.randrange(0,R)
    ce=random.randrange(0,C)
    k+=1
    if k>100:
        break'''
rs=cs=0
re,ce=R-1,C-1
p[rs][cs]=p[re][ce]=0

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

def countbomb(a,b,maze):        #找出炸開路徑方位
    lis=list()
    if a-1>=0 and p[a-1][b]==1 and len(count(a-1,b,'v',maze))==1:
        lis.append(1)
    if b-1>=0 and p[a][b-1]==1 and len(count(a,b-1,'v',maze))==1:
        lis.append(2)
    if a+1<R and p[a+1][b]==1 and len(count(a+1,b,'v',maze))==1:
        lis.append(3)
    if b+1<C and p[a][b+1]==1 and len(count(a,b+1,'v',maze))==1:
        lis.append(4)
    return lis

r,c=rs,cs
way=[[r,c]]
i=back=0

def add_d(maze):            #將沒有方向list的加入
    if len(way[i])==2:
        way[i].append(count(way[i][0],way[i][1],0,maze))

while r!=re or c!=ce :          #讓迷宮有答案
    p[r][c]='v'
    add_d(p)
    if len(way[i][2])==0:
        while len(way[i][2])==0:
            if i==back:         #開路
                bomb=random.randrange(0,len(way))
                while len(countbomb(way[bomb][0],way[bomb][1],p))==0:
                    del way[bomb]
                    bomb=random.randrange(0,len(way))
                match random.choice(countbomb(way[bomb][0],way[bomb][1],p)):
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
                add_d(p)
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

while r!=re or c!=ce :          #找到迷宮的解答
    answer[r][c]='v'
    add_d(answer)
    if len(way[i][2])==0:
        while len(way[i][2])==0:
            answer[r][c]=0
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

answer[rs][cs]='s'
answer[re][ce]='e'
print("answer:")
for row in answer :
    print(*row)
