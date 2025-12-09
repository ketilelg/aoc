import sys
from functools import cache

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

xset=set()
yset=set()
for l in inp:
    x,y=map(int,l.split(","))
    xset.add(x)
    yset.add(y)

xs=sorted(xset)
ys=sorted(yset)

xr=dict()
for i in range(len(xs)):
    xr[xs[i]]=i
yr=dict()
for i in range(len(ys)):
    yr[ys[i]]=i

tiles=[]
for l in inp:
    x,y=map(int,l.split(","))
    tiles.append((xr[x],yr[y]))


lines=[]
for i in range(len(tiles)):
    nn=tiles[i-1] #stilig måte å begå løkke. takk til Peder
    sx=tiles[i][0]
    sy=tiles[i][1] 
    nx=nn[0]
    ny=nn[1]
    if sx!=nx: #vi trenger kun horisontale linjer
        lines.append(((sx,sy),(nx,ny)))

lines.sort(key=lambda x: x[0][1])

# for l in lines:
#     print("l",l)
# def inline(lines,x1,y1,x2,y2): #overlapper rektangelet med en linje?
#     for l in lines:
#         sx=min(l[0][0],l[1][0])
#         ex=max(l[0][0],l[1][0])
#         sy=min(l[0][1],l[1][1])
#         ey=max(l[0][1],l[1][1])
#         if ((((x1 >= sx) and (x1 <= ex)) or ((x2>=sx) and ((x2 <= ex))) or ((x1 < sx) and (x2 > ex))) and 
#             (((y1 >= sy) and (y1 <= ey)) or ((y2>=ey) and ((y2 <= ey))) or ((y1 < sy) and (y2 > ey)))):
#             return True
#     return False

# def online(l,x,y): #is x,y on line?
#     sx=min(l[0][0],l[1][0])
#     ex=max(l[0][0],l[1][0])
#     sy=min(l[0][1],l[1][1])
#     ey=max(l[0][1],l[1][1])
#     return ((x>=sx) and (x<=ex) and (y>=sy) and (y<=ey))

@cache
def inside(x,y): #er x,y innenfor perimeteren?
    nh=0
    for l in lines: #alle linjer er horisontale
        sx=min(l[0][0],l[1][0])
        ex=max(l[0][0],l[1][0])
        ly=l[0][1]
        if (y>=ly) and (x>=sx) and (x<=ex):
            nh+=1 
        if ly>y: #ikke fler linjer å sjekke i denne omgang
            break
    return nh%2==1


rects=[]
for i in range(len(tiles)):
    for j in range(i+1,len(tiles)):
        sx=min(tiles[i][0],tiles[j][0])
        sy=min(tiles[i][1],tiles[j][1])
        ex=max(tiles[i][0],tiles[j][0])
        ey=max(tiles[i][1],tiles[j][1])
        a=(xs[ex]-xs[sx]+1)*(ys[ey]-ys[sy]+1)
        rects.append((a,sx,sy,ex,ey))
        if a > p1:
            p1=a

for r in sorted(rects,reverse=True):
    a=r[0]
    sx=r[1]
    sy=r[2]
    ex=r[3]
    ey=r[4]
#    print("testing",a,sx,sy,ex,ey)
    ins=True
    for x in range(sx,ex):
        if not inside(x+0.5,sy+0.5) or not inside(x+0.5,sy+0.5):
            ins=False
            break
    for y in range(sy,ey):
        if not inside(sx+0.5,y+0.5) or not inside(ex-0.5,y+0.5):
            ins=False
            break
    if ins:
        p2=a                    
        break

print("1:",p1)
print("2:",p2)
