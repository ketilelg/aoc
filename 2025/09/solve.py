import sys
from collections import defaultdict
import re
from functools import cache


with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

minx=miny=10000
maxx=maxy=0
tiles=[]
for l in inp:
#    print("l",l)
    x,y=map(int,l.split(","))
    tiles.append((x,y))
    if x<minx:
        minx=x
    elif x > maxx:
        maxx=x
    if y<miny:
        miny=y
    elif y > maxy:
        maxy=y

print("mm",minx,miny,maxx,maxy)

lines=[]
for i in range(len(tiles)-1):
    lines.append((tiles[i],tiles[i+1]))
lines.append((tiles[0],tiles[-1]))

def inline(x1,y1,x2,y2): #overlapper rektangelet med en linje?
    for l in lines:
        sx=min(l[0][0],l[1][0])
        ex=max(l[0][0],l[1][0])
        sy=min(l[0][1],l[1][1])
        ey=max(l[0][1],l[1][1])
        if ((((x1 >= sx) and (x1 <= ex)) or ((x2>=sx) and ((x2 <= ex))) or ((x1 < sx) and (x2 > ex))) and 
            (((y1 >= sy) and (y1 <= ey)) or ((y2>=ey) and ((y2 <= ey))) or ((y1 < sy) and (y2 > ey)))):
            print("inline",x1,y1,x2,y2,sx,sy,ex,ey)
            return True
    return False

outside=[]
explores=[(0,0)] #list of corners to explore..
while explores:
    x,y=explores.pop()
    print("xy",x,y)
    nx=x
    ny=y
    while nx<=maxx and not inline(x,y,nx,ny):
        nx+=1    
    if nx!=x:
        nx-=1
    while ny<=maxy and not inline(x,y,nx,ny):
        ny+=1
    if ny!=y:
        ny-=1
    print("nn",nx,ny)
    if ((x!=nx) or (y!=ny)) and ((nx <= maxx) and (ny <= maxy)):
        outside.append((x,y,nx,ny))
    #    if x!=nx:
        explores.append((nx+1,y))
    #        if y!=ny:
        explores.append((nx+1,ny+1))
    #    if y!=ny:
        explores.append((x+1,ny+1))

for o in outside:
    print("o",o)
for i in range(len(tiles)):

    for j in range(i+1,len(tiles)):
        a=(abs(tiles[i][0]-tiles[j][0])+1)*(abs(tiles[i][1]-tiles[j][1])+1)
        if a > p1:
            p1=a

        if a > p2:
            #iterer over alle andre rektangler, og finn overlapp, om arealet av sammenlagt overlapp
            #er lik a, er a brukbar for p2
            #eller: om noe av dette overlapper "utside"-lista er det ikke en kandidat
            pass

print("1:",p1)
print("2:",p2)
