import random

r=int(input())
c=int(input())  #迷宮大小
p=list()
for i in range(r):
    p.append(list())
    for j in range(c):
        p[i].append(random.choice([0,1]))   #生成初始迷宮
r0=random.randrange(0,r)
c0=random.randrange(0,c)
r1=random.randrange(0,r)
c1=random.randrange(0,c)
while r0==r1 and c0==c1:
    r1=random.randrange(0,r)
    c1=random.randrange(0,c)    #生成開始點0及結束點1
for row in p:
    print(*row)