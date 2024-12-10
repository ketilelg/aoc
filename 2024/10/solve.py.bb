import sys
import copy
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    map = list(map(list,f.read().strip().split("\n")))

p1=0
p2=0

w=len(map)
h=len(map[0])

ratings=[]
#aargh

for y in range(h):
    ratings.append([])
    for x in range(w):
        map[y][x]=int(map[y][x])
        ratings[y].append(0)

print("r",ratings)

def printmap(m):
    for y in range(h):
        for x in range(w):
            print(m[y][x],end="")
        print("")

print("mmm",map)
printmap(map)

peaks=defaultdict(set)

def findtrails(sx,sy,x,y,level):
    if(map[y][x] != level):
        return
    elif(level==9):
        peaks[(x,y)].add((sx,sy))
        ratings[sy][sx]+=1
    else:
        for move in [(-1,0),(0,-1),(1,0),(0,1)]:
            nx=x+move[0]
            ny=y+move[1]
            if(0<=nx<w and 0<=ny<h):
                findtrails(sx,sy,nx,ny,level+1)
    
for x in range(w):
    for y in range(h):
        findtrails(x,y,x,y,0)

print("pp",peaks)
print("rr",ratings)
for p in peaks:
    print("p",p,len(peaks[p]))
    p1+=len(peaks[p])

for l in ratings:
    for p in l:
        p2+=p
print("1:",p1)
print("2:",p2)
