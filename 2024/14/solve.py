import sys
import re
import copy

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
    print("dsf",px,py,nx,ny)
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
            print(c,end="")
        print("<")


def testgen(gen):
    rmap=[["."]*(maxx+1) for i in range(maxy+1)]
    ul=ur=ll=lr=0
    for px,py,vx,vy in robots:
        nx=(px+(gen*vx))%(maxx+1)
        ny=(py+(gen*vy))%(maxy+1)
        rmap[ny][nx]="R"
        if nx < midx and ny < midy:
            ul+=1
        if nx > midx and ny < midy:
            ur+=1
        if nx > midx and ny > midy:
            lr+=1
        if nx < midx and ny > midy:
            ll+=1
    print("\ngen",gen)
    printmap(rmap)
    return False # i see no reasonable automated test.. 

while not testgen(p2):
    p2+=1

print("1:",p1)
print("2:",p2)
