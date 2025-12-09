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
vlines=[]
for i in range(len(tiles)):
    nn=tiles[i-1] #stilig måte å begå løkke. takk til Peder
    sx=tiles[i][0]
    sy=tiles[i][1] 
    nx=nn[0]
    ny=nn[1]
    if sx!=nx: #vi trenger kun horisontale linjer
        lines.append(((sx,sy),(nx,ny)))
    else:
        vlines.append(((sx,sy),(nx,ny)))
lines.sort(key=lambda x: x[0][1])
vlines.sort(key=lambda x: x[0][0])

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

@cache
def lineinside(lsx,lsy,lex,ley): #er linjen inne eller ute?
    if not inside(lsx,lsy):
        return False
    if not inside(lex,ley):
        return False
    if lsy==ley: #linje er horisontal, se etter vertikale kryss
        for l in vlines:
            x=l[0][0]
            if x>lex:
                break
            sy=min(l[0][1],l[1][1])
            ey=max(l[0][1],l[1][1])
            if (lsx<=x) and (lex>=x) and (lsy>=sy) and (ley<=ey):
                return False
    else: #linja er vertikal, se etter kryss med horisontale linjer
        for l in lines:
            y=l[0][1]
            if y>ley:
                break
            sx=min(l[0][0],l[1][0])
            ex=max(l[0][0],l[1][0])
            if (lsx<=ex) and (lex>=sx) and (lsy<=y) and (ley>=y):
                return False
    return True

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
    a,sx,sy,ex,ey=r 
    if lineinside(sx+0.5,sy+0.5,ex-0.5,sy+0.5) and lineinside(sx+0.5,ey-0.5,ex-0.5,ey-0.5) and lineinside(sx+0.5,sy+0.5,sx+0.5,ey-0.5) and lineinside(ex-0.5,sy+0.5,ex-0.5,ey-0.5): 
        p2=a                    
        break


print("1:",p1)
print("2:",p2)
