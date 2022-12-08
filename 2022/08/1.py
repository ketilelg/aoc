#!/usr/bin/python3

r=[]
with open('input') as f:
    for line in f:
        r.append(line.strip())

def isvis(r,x,y):
    nv=0
    n=False
    for i in range(x):
        if r[i][y]>=r[x][y]:
            n=True
            break
    if not n:
        return 1
    n=False
    for i in range(x+1,len(r)):
        if r[i][y]>=r[x][y]:
            n=True
            break
    if not n:
        return 1
    n=False
    for i in range(y):
        if r[x][i]>=r[x][y]:
            n=True
            break
    if not n:
        return 1
    n=False
    for i in range(y+1,len(r[x])):
        if r[x][i]>=r[x][y]:
            n=True
            break
    if not n:
        return 1
    return 0

def ssc(r,x,y):
    nv=0
    mh=r[x][y]
    vd1=vd2=vd3=vd4=0
    for i in range(x+1,len(r)):
        vd1+=1
        if r[i][y]>=mh:
            break
    for i in range(x-1,-1,-1):
        vd2+=1
        if r[i][y]>=mh:
            break
    for i in range(y+1,len(r[x])):
        vd3+=1
        if r[x][i]>=mh:
            break
    for i in range(y-1,-1,-1):
        vd4+=1
        if r[x][i]>=mh:
            break
    return vd1*vd2*vd3*vd4

tv=0
md=0
for x in range(1,len(r)-1):
    for y in range(1,len(r[0])-1):
        tv+=isvis(r,x,y)
        d=ssc(r,x,y)
        if md<d:
            md=d

print("p1:",tv+2*len(r)+2*len(r[0])-4)
print("p2:",md)
