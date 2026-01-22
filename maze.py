import random
import copy

R=int(input())      #迷宮大小
C=int(input())
maze=list()

def first_maze(maze):      #生成初始迷宮
    for i in range(R):
        maze.append(list())
        for j in range(C):
            maze[i].append(random.choice([0,1]))
            if i>0 and j>0 and maze[i][j]==0 and maze[i-1][j]==0 and maze[i][j-1]==0 and maze[i-1][j-1]==0 :
                match random.randrange(1,5) :
                    case 1 :
                        maze[i][j]=1
                    case 2 :
                        maze[i-1][j]=1
                    case 3 :
                        maze[i][j-1]=1
                    case 4 :
                        maze[i-1][j-1]=1
    return maze

def start_end(maze):
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
    maze[rs][cs]=maze[re][ce]=0
    return maze,rs,cs,re,ce


def count(a,b,item,maze):        #找出item方位
    length=0
    if a-1>=0 and maze[a-1][b]==item:
        length+=1
    if b-1>=0 and maze[a][b-1]==item:
        length+=1
    if a+1<R and maze[a+1][b]==item:
        length+=1
    if b+1<C and maze[a][b+1]==item:
        length+=1
    return length

def countbomb(a,b,item,maze):        #找出炸開路徑方位
    dies=list()
    if a-1>=0 and maze[a-1][b]==1 and count(a-1,b,item,maze)==1:
        dies.append(1)
    if b-1>=0 and maze[a][b-1]==1 and count(a,b-1,item,maze)==1:
        dies.append(2)
    if a+1<R and maze[a+1][b]==1 and count(a+1,b,item,maze)==1:
        dies.append(3)
    if b+1<C and maze[a][b+1]==1 and count(a,b+1,item,maze)==1:
        dies.append(4)
    return dies

def add_d(a,b,maze,path,item,i):            #將沒有方向list的加入
    if len(path[i])==2:
        lis=list()
        if a-1>=0 and maze[a-1][b]!=1 and maze[a-1][b]<=item:
            lis.append(1)
        if b-1>=0 and maze[a][b-1]!=1 and maze[a][b-1]<=item:
            lis.append(2)
        if a+1<R and maze[a+1][b]!=1 and maze[a+1][b]<=item:
            lis.append(3)
        if b+1<C and maze[a][b+1]!=1 and maze[a][b+1]<=item:
            lis.append(4)
        path[i]["dirs"]=lis

def real_maze(maze):          #形成一個真正有路線的迷宮
    allrc=list()
    mark=2
    for a in range(R):
        for b in range(C):
            if maze[a][b]==0:
                allrc.append([a,b])
    for nothing in range(len(allrc)):
        r,c=random.choice(allrc)
        allrc.remove([r,c])
        if maze[r][c]==0:
            path=[{"r":r, "c":c}]
            i=back=0
            while len(path)>0:
                maze[r][c]=mark
                add_d(r,c,maze,path,mark-1,i)
                if len(path[i]["dirs"])==0:
                    while len(path[i]["dirs"])==0:
                        if i==back:
                            bomb=random.randrange(0,len(path))
                            while len(countbomb(path[bomb]["r"],path[bomb]["c"],mark,maze))==0:
                                del path[bomb]
                                if len(path)==0:
                                    break
                                bomb=random.randrange(0,len(path))
                            if len(path)==0:
                                break
                            match random.choice(countbomb(path[bomb]["r"],path[bomb]["c"],mark,maze)):
                                case 1:
                                    r,c=path[bomb]["r"]-1,path[bomb]["c"]
                                case 2:
                                    r,c=path[bomb]["r"],path[bomb]["c"]-1
                                case 3:
                                    r,c=path[bomb]["r"]+1,path[bomb]["c"]
                                case 4:
                                    r,c=path[bomb]["r"],path[bomb]["c"]+1
                            maze[r][c]=0
                            path.append({"r":r, "c":c})
                            i=len(path)-1
                            back=i
                            add_d(r,c,maze,path,mark-1,i)
                            break
                        i-=1
                        r,c=path[i]["r"],path[i]["c"]
                    continue
                d=random.choice(path[i]["dirs"])
                path[i]["dirs"].remove(d)
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
                path.insert(i,{"r":r, "c":c})
            mark+=1
    for x in range(R):
        for y in range(C):
            if maze[x][y]>1:
                maze[x][y]=0
    return maze

def better_maze(maze):        #優化迷宮
    for i in range(R):
        for j in range(C):
            if i>0 and j>0 and maze[i][j]==0 and maze[i-1][j]==0 and maze[i][j-1]==0 and maze[i-1][j-1]==0 :
                turn1=list()
                if count(i,j,0,maze)==2:
                    turn1.append([i,j])
                if count(i-1,j,0,maze)==2:
                    turn1.append([i-1,j])
                if count(i,j-1,0,maze)==2:
                    turn1.append([i,j-1])
                if count(i-1,j-1,0,maze)==2:
                    turn1.append([i-1,j-1])
                if len(turn1)>=1:
                    x=random.randrange(0,len(turn1))
                    maze[turn1[x][0]][turn1[x][1]]=1
    return maze

def answer_shortest_maze(maze,rs,cs,re,ce):          #找出迷宮最短的解答
    r,c=rs,cs
    path=[{"r":r, "c":c}]
    i=0
    shortest=R*C
    shortest_path=list()

    while i>=0 :
        maze[r][c]=2
        add_d(r,c,maze,path,0,i)
        if len(path[i]["dirs"])==0:
            while len(path[i]["dirs"])==0:
                maze[r][c]=0
                del path[-1]
                i-=1
                if i<0:
                    break
                r,c=path[i]["r"],path[i]["c"]
            continue
        match path[i]["dirs"].pop():
            case 1:
                r-=1
            case 2:
                c-=1
            case 3:
                r+=1
            case 4:
                c+=1
        if r==re and c==ce:
            print(666)
            if len(path)<shortest:
                shortest=len(path)
                shortest_path=copy.deepcopy(path)
            r,c=path[i]["r"],path[i]["c"]
            continue
        i+=1
        path.insert(i,{"r":r, "c":c})

    maze[rs][cs]='s'
    maze[re][ce]='e'
    answer_shortest=copy.deepcopy(maze)
    for rc in shortest_path[1:]:
        answer_shortest[rc["r"]][rc["c"]]='v'
    return maze,shortest,answer_shortest

maze=first_maze(maze)
maze,rs,cs,re,ce=start_end(maze)
maze=real_maze(maze)
maze=better_maze(maze)
maze,shortest,answer_shortest=answer_shortest_maze(maze,rs,cs,re,ce)
while shortest<(abs(rs-re)+abs(cs-ce))*1:           #避免迷宮太容易
    maze,shortest,answer_shortest=answer_shortest_maze(maze,rs,cs,re,ce)
print("maze:")
for row in maze:
    print(*row)
print("answer(shortest):")
for row in answer_shortest:
    print(*row)
print(shortest)
