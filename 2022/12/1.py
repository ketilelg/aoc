#!/usr/bin/python3

import sys
sys.setrecursionlimit(3000)
with open('input') as f:
    map = f.read().strip().split("\n")

w=len(map[0])
h=len(map)

ex = ey= sx = sy = -1
while sx < 0:
    sy+=1
    sx=map[sy].find("S")
while ex < 0:
    ey+=1
    ex=map[ey].find("E")

map[sy] = map[sy].replace("S","`")
map[ey] = map[ey].replace("E","{")

depth= [[10000] * w for i in range(h)]

def seek(x,y,v,d):

    if d < depth[y][x]:

        depth[y][x] = d

        if map[y][x] == "`":
            return

        d+=1
        for i in -1,1:
            nx=x+i
            if nx >= 0 and nx < w and d < depth[y][nx] and ord(map[y][nx])+1 >= ord(v):
                seek(nx,y,map[y][nx],d)
        for i in -1,1:
            ny=y+i
            if ny >= 0 and ny < h and d < depth[ny][x] and ord(map[ny][x])+1 >= ord(v):
                seek(x,ny,map[ny][x],d)



seek(ex,ey,map[ey][ex],0)
print("p1",depth[sy][sx])
sa=10000
for fx in range(w):
    for fy in range(h):
        if map[fy][fx] == "a":
            if depth[fy][fx] < sa:
                sa = depth[fy][fx]
print("p2",sa)
