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
xset=set()
yset=set()
for l in inp:
    x,y=map(int,l.split(","))
    xset.add(x)
    yset.add(y)

xs=sorted(xset)
ys=sorted(yset)
print("ss",xs,ys)
xr=dict()
for i in range(len(xs)):
    xr[xs[i]]=i
yr=dict()
for i in range(len(ys)):
    yr[ys[i]]=i
print("sdf",xr,yr)


for l in inp:
    x,y=map(int,l.split(","))
    print("xy",x,y)
    tiles.append((xr[x],yr[y]))


lines=[]
for i in range(len(tiles)):
    nn=tiles[i-1]
    sx=tiles[i][0]
    sy=tiles[i][1] 
    nx=nn[0]
    ny=nn[1]  
    lines.append(((sx,sy),(nx,ny)))
    print("lll",i,sx,sy,nx,ny)
#     if sx==nx: #vert line
# #        lines.append(((sx,min(sy,ny)+1),(sx,max(sy,ny)-1)))
# #    else:
# #        lines.append(((min(sx,nx)+1,ny),((max(sx,nx)+1,ny))))
#         if sy<ny:
#             lines.append(((sx,sy),(nx,ny-1)))
#         else:                    
#             lines.append(((sx,sy),(nx,ny+1)))
#     else: #horizontal line 
#         if sx<nx:
#             lines.append(((sx,sy),(nx-1,ny)))
#         else:
#             lines.append(((sx,sy),(nx+1,ny)))

for l in lines:
    print("l",l)

def inline(lines,x1,y1,x2,y2): #overlapper rektangelet med en linje?
    for l in lines:
        sx=min(l[0][0],l[1][0])
        ex=max(l[0][0],l[1][0])
        sy=min(l[0][1],l[1][1])
        ey=max(l[0][1],l[1][1])
        if ((((x1 >= sx) and (x1 <= ex)) or ((x2>=sx) and ((x2 <= ex))) or ((x1 < sx) and (x2 > ex))) and 
            (((y1 >= sy) and (y1 <= ey)) or ((y2>=ey) and ((y2 <= ey))) or ((y1 < sy) and (y2 > ey)))):
#            print("inline",x1,y1,x2,y2,sx,sy,ex,ey)
            return True
    return False

def online(l,x,y): #is x,y on line?
    sx=min(l[0][0],l[1][0])
    ex=max(l[0][0],l[1][0])
    sy=min(l[0][1],l[1][1])
    ey=max(l[0][1],l[1][1])
    return ((x>=sx) and (x<=ex) and (y>=sy) and (y<=ey))

def inside(lines,x,y): #is x,y inside perimeter drawn by lines?
    nh=0
    nv=0
    for l in lines:
#        if online(l,x,y):
#            return True
        sx=min(l[0][0],l[1][0])
        ex=max(l[0][0],l[1][0])
        sy=min(l[0][1],l[1][1])
        ey=max(l[0][1],l[1][1])
        if (sy==ey) and (y>=sy) and (x>=sx) and (x<=ex):
            nh+=1 #hor linje
#            if y==1 and x==2:
#                print("ahl",nh,nv,sx,sy,ex,ey,x,y)
#        if ((sx==ex) and (x>=sx) and (y>=sy) and (y<=ey)):
#            nv+=1
#            if y==1 and x==2:
#                print("bhl",nh,nv,sx,sy,ex,ey,x,y)
#    if y==1 and x==2:
#        print("hl",nh,nv,sx,sy,ex,ey,x,y)
#    return False
    ii=(nh%2==1)# and (nv%2==1)
#    if ii:
#        print("inside",x,y,nh,ii)
    return ii


# for y in range(0,12):
#     for x in range(0,12):
#         if inside(lines,x+0.1,y+0.1):
#             print("i",end="")
#         elif inside(lines,x-0.1,y-0.1):
#             print("j",end="")
#         elif inside(lines,x+0.1,y-0.1):
#             print("k",end="")
#         elif inside(lines,x-0.1,y+0.1):
#             print("l",end="")
#         else:
#             print(".",end="")
#     print("")        
        
# exit()

outside=[]

for o in outside:
    print("o",o)

for i in range(len(tiles)):

    for j in range(i+1,len(tiles)):
        sx=min(tiles[i][0],tiles[j][0])
        sy=min(tiles[i][1],tiles[j][1])
        ex=max(tiles[i][0],tiles[j][0])
        ey=max(tiles[i][1],tiles[j][1])
        print("ff")
        a=(xs[ex]-xs[sx]+1)*(ys[ey]-ys[sy]+1)
        if a > p1:
            p1=a

        if a > p2:
            print("testing",a,i,j,sx,sy,ex,ey)
            ins=True
            for x in range(sx,ex):
                if not inside(lines,x+0.5,sy+0.5) or not inside(lines,x+0.5,ey-0.5):
                    ins=False
                    break
            for y in range(sy,ey):
                if not inside(lines,sx+0-5,y+0.5) or not inside(lines,ex-0.5,y+0.5):
                    ins=False
                    break
            if ins:
                p2=a                    

print("1:",p1)
print("2:",p2)
