#!/usr/bin/python3

import numpy as np

f=open('input')
input=f.read().strip()

minx=miny=minz=10000
maxx=maxy=maxz=0

for c in input.split("\n"):
    x,y,z=map(int,c.split(","))
    if x>maxx:
        maxx=x
    if y>maxy:
        maxy=y
    if z>maxz:
        maxz=z
    if x<minx:
        minx=x
    if y<miny:
        miny=y
    if z<minz:
        minz=z


w=maxx+1
h=maxy+1
d=maxz+1

world=np.full((w,h,d), False)

for c in input.split("\n"):
    x,y,z=map(int,c.split(","))
    world[x][y][z]=True



def isclear(x,y,z):
    #is the coordinate x,y,z clear (either outside or not set)?
    if x<minx or x > maxx or y < miny or y > maxy or z < minz or z > maxz:
        return True
    else:
        return not world[x][y][z]

def nclear(x,y,z):
    #how many clear neighbors does xyz have?
    nx=0
    if isclear(x-1,y,z):
        nx+=1
    if isclear(x+1,y,z):
        nx+=1
    if isclear(x,y-1,z):
        nx+=1
    if isclear(x,y+1,z):
        nx+=1
    if isclear(x,y,z-1):
        nx+=1
    if isclear(x,y,z+1):
        nx+=1
    return nx
    
    
p1=0
for x in range(minx,maxx+1):
    for y in range(miny,maxy+1):
        for z in range(minz,maxz+1):
            if world[x][y][z]:
                p1 += nclear(x,y,z)


print("p1:",p1)


def floodfill(x,y,z):
    #floodfills from xyz, returns true if edge is hit..
    if x<minx or x > maxx or y < miny or y > maxy or z < minz or z > maxz:
        return True
    elif not nworld[x][y][z]:
        nworld[x][y][z]=True
        if floodfill(x-1,y,z):
            return True
        if floodfill(x+1,y,z):
            return True
        if floodfill(x,y-1,z):
            return True
        if floodfill(x,y+1,z):
            return True
        if floodfill(x,y,z-1):
            return True
        if floodfill(x,y,z+1):
            return True
        return False
    else:
        return False

    
nworld=np.copy(world)
for x in range(minx,maxx+1):
    for y in range(miny,maxy+1):
        for z in range(minz,maxz+1):
            if not nworld[x][y][z]:
                if floodfill(x,y,z):
                    nworld=np.copy(world)
                else:
                    world=np.copy(nworld)

p2=0
for x in range(minx,maxx+1):
    for y in range(miny,maxy+1):
        for z in range(minz,maxz+1):
            if world[x][y][z]:
                p2 += nclear(x,y,z)

print("p2:",p2)
