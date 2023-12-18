import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    input =  [s.split(" ") for s in f.read().strip().split("\n")]

x=0
y=0
x2=0
y2=0
minx=maxx=miny=maxy=0

segments=[]
lsegs=[]
elen2=0

for i in input:
    ox=x
    oy=y
    ox2=x2
    oy2=y2
    d=i[0]
    l=int(i[1])
    c2=int(i[2][2:-2],16)
    d2=i[2][-2:-1]
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
    segments.append(((ox,oy),(x,y)))
    if(x<minx):
        minx=x
    if(x>maxx):
        maxx=x
    if(y<miny):
        miny=y
    if(y>maxy):
        maxy=y
    print("c2",c2,d2)
    if(d2=="0"):
        x2+=c2
    elif(d2=="1"):
        y2+=c2
    elif(d2=="2"):
        x2-=c2
    elif(d2=="3"):
        y2-=c2
    elen2+=c2
    lsegs.append(((ox2,oy2),(x2,y2)))
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
elen=0
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
    elen+=l
    for xx in range(min(px,x),max(px,x)+1):
        for yy in range(min(py,y),max(py,y)+1):
            mmap[yy][xx]="#"


        
printm(mmap)

print("mm",minx,miny,maxx,maxy)
mmap[0][0]="O"

def fill():
    nw=(maxx-minx)+3
    nh=(maxy-miny)+3
    n=1
    while(n > 0):
        n=0
        for x in range(nw):
            for y in range(nh):
#                print("xy",x,y)
                if(mmap[y][x] == "."):
                    if(((x-1>= 0) and (mmap[y][x-1]=="O")) or
                       ((x+1< nw) and (mmap[y][x+1]=="O")) or
                       ((y-1>= 0) and (mmap[y-1][x]=="O")) or
                       ((y+1< nh) and (mmap[y+1][x]=="O"))):
                        mmap[y][x]="O"
                        n+=1
# fill()
                        
printm(mmap)

vol=0
ovol=0
evol=0
dvol=0
for l in mmap:
    for c in l:
        if(c!="O"):
            vol+=1
        else:
            ovol+=1
        if(c=="."):
            dvol+=1
        if(c=="#"):
            evol+=1
s1=vol

print("s",segments)

def area(s,l):
    return int(0.5* abs(sum(x0*y1 - x1*y0 for ((x0,y0), (x1,y1)) in s))) +((l/2))+1


s1=area(segments,elen)
print("v",vol,ovol,elen,evol,dvol)
print("1:", int(s1))
#36841 too low
#72457 too high

print("a2",area(lsegs,elen2))
print("2:", int(s2))

