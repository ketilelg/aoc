import sys
from collections import defaultdict

tmap=[]
with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    for line in f:
        tmap.append(list(map(int,list(line.strip()))))

p1=p2=0

h=len(tmap)
w=len(tmap[0])

ratings=[[0]*w for i in range(h)]

def printmap(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            print(m[y][x],end="")
        print("")

peaks=defaultdict(set)

def findtrails(sx,sy,x,y,level):
    if(tmap[y][x] != level):
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
#find all trails:    
for x in range(w):
    for y in range(h):
        findtrails(x,y,x,y,0)
#sum up peaks for part 1:
for p in peaks:
    p1+=len(peaks[p])
#sum ratings for part 2:
for l in ratings:
    for p in l:
        p2+=p

print("1:",p1)
print("2:",p2)