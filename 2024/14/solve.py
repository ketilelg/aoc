import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

robots=[]

minx=miny=100000000000
maxx=maxy=0
for l in inp:
    px,py,vx,vy=map(int,re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)",l)[0])
    minx=min(minx,px)
    maxx=max(maxx,px)
    miny=min(miny,py)
    maxy=max(maxy,py)
    robots.append([px,py,vx,vy])


gens=100
midx=maxx//2
midy=maxy//2
ul=ur=ll=lr=0
for px,py,vx,vy in robots:
    nx=(px+(gens*vx))%(maxx+1)
    ny=(py+(gens*vy))%(maxy+1)
    if nx < midx and ny < midy:
        ul+=1
    if nx > midx and ny < midy:
        ur+=1
    if nx > midx and ny > midy:
        lr+=1
    if nx < midx and ny > midy:
        ll+=1

p1=ul*ur*ll*lr

def printmap(m):
    for l in m:
        for c in l:
            if(c>0):
                print(c,end="")
            else:
                print(" ",end="")
        print("")


def nneighs(rmap):
    #returns number of robots with more than 1 neighbour
    #2nd gen assumtion: number of neighbors is high when picture is formed
    nei=0
    for y in range(maxy+1):
        for x in range(maxx+1):
            for dx in (-1,0,1):
                nn=0
                for dy in (-1,0,1):
                    if 0<=x+dx<=maxx and 0<=y+dy<=maxy and rmap[y+dy][x+dx]>0:
                        nn+=1
            if nn>1:
                nei+=1
    return nei


def testgen(gen):
    rmap=[[0]*(maxx+1) for i in range(maxy+1)]
    allones=True # no points with more than one robot
    for px,py,vx,vy in robots:
        nx=(px+(gen*vx))%(maxx+1)
        ny=(py+(gen*vy))%(maxy+1)
        rmap[ny][nx]+=1
        allones = allones and rmap[ny][nx] < 2
    n=nneighs(rmap)
    print("gen",gen,n)
    allones=n>int(len(robots)/2)
    if n>=100:
        print("\ngen",gen)
        printmap(rmap)
    return allones # assumption (stolen from Stein): no overlapping robots==picture

while not testgen(p2):
    p2+=1

print("1:",p1)
print("2:",p2)
