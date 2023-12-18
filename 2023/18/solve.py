import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    input =  [s.split(" ") for s in f.read().strip().split("\n")]

x=0
y=0
x2=0
y2=0

segments=[]
lsegs=[]
elen2=0
elen=0

for i in input:
    ox=x
    oy=y
    ox2=x2
    oy2=y2
    d=i[0]
    l=int(i[1])
    elen+=l
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

def area(s,l):
    return int(0.5* abs(sum(x0*y1 - x1*y0 for ((x0,y0), (x1,y1)) in s))) +((l/2))+1


s1=area(segments,elen)

print("1:", int(s1))

s2=area(lsegs,elen2)
print("2:", int(s2))

