import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    input =  [s.split(" ") for s in f.read().strip().split("\n")]

x=0
y=0
minx=maxx=miny=maxy=0

for i in input:
    d=i[0]
    l=int(i[1])
    c=i[2]
    if(d=="R"):
        x+=l
    elif(d=="U"):
        y-=l
    elif(d=="L"):
        x-=l
    elif(d=="D"):
        y+=l
    else:
        print("wtf")
    if(x<minx):
        minx=x
    if(x>maxx):
        maxx=x
    if(y<miny):
        miny=y
    if(y>maxy):
        maxy=y

print("end",x,y,minx,miny,maxx,maxy)

mmap=[["." for x in range(minx,maxx+3)] for y in range(miny,maxy+3)] 

def printm(m):
#    print("\033c")
    for l in m:
        for c in l:
            print(c,end="")
        print()

x=1-minx
y=1-miny
for i in input:
    d=i[0]
    l=int(i[1])
    c=i[2]
    px=x
    py=y
    if(d=="R"):
        x+=l
    elif(d=="U"):
        y-=l
    elif(d=="L"):
        x-=l
    elif(d=="D"):
        y+=l
    else:
        print("wtf")
    for xx in range(min(px,x),max(px,x)+1):
        for yy in range(min(py,y),max(py,y)+1):
            mmap[yy][xx]="#"


        
printm(mmap)

print("mm",minx,miny,maxx,maxy)
mmap[0][0]="O"

def fill():
    nw=(maxx-minx)+2
    nh=(maxy-miny)+2
    n=1
    while(n > 0):
        n=0
        for x in range(nw+1):
            for y in range(nh+1):
                if(mmap[y][x] == "."):
                    if(((x-1>= 0) and (mmap[y][x-1]=="O")) or
                       ((x+1< nh) and (mmap[y][x+1]=="O")) or
                       ((y-1>= 0) and (mmap[y-1][x]=="O")) or
                       ((y+1< nw) and (mmap[y+1][x]=="O"))):
                        mmap[y][x]="O"
                        n+=1
fill()
                        
printm(mmap)

vol=0
for l in mmap:
    for c in l:
        if(c!="."):
            vol+=1
s1=vol
print("1:", int(s1))
#36841 too low


print("2:", int(s2))

