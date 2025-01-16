import sys
import re
import numpy as np

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

map=np.zeros((1000,1000)).astype(bool)
map2=np.zeros((1000,1000))
for b in inp:
    command,ssx,ssy,slx,sly=re.match(r"^(\D+) (\d+),(\d+) through (\d+),(\d+)",b).groups()
    sx=int(ssx)
    sy=int(ssy)
    lx=int(slx)
    ly=int(sly)
    print("ff",command,sx,sy,lx,ly)
    for x in range(sx,lx+1):
        for y in range(sy,ly+1):
            if command=="turn off":
                map[y][x]=False
                if map2[y][x]>0:
                    map2[y][x]-=1
            elif command=="turn on":
                map[y][x]=True
                map2[y][x]+=1
            else:
                map[y][x]=not map[y][x]
                map2[y][x]+=2


for x in range(1000):
    for y in range(1000):
        if map[y][x]:
            p1+=1
        p2+=map2[y][x]


print("1:",p1)
print("2:",p2)
