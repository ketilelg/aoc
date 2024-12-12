import sys
import copy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(list,f.read().strip().split("\n")))

p1=p2=0

h=len(inp)
w=len(inp[0])

for l in inp:
    l.insert(0,".")
    l.append(".")
inp.insert(0,["."] * (w+2))
inp.append(["."] * (w+2))

visited=copy.deepcopy(inp)
ids=copy.deepcopy(inp)

def printmap(m):
    for l in m:
        for c in l:
            print(c,end="")
        print("<")

def findarea(type,x,y,id):
    area=1
    peri=0
    corners={}
    visited[y][x]=" "
    ids[y][x]=id
    for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
        nx=x+dx
        ny=y+dy
        if(inp[ny][nx]==type and visited[ny][nx] != " "):
            a,p,c=findarea(type,nx,ny,id)
            area+=a
            peri+=p
            corners.update(c)
        elif inp[ny][nx]!=type:
            peri+=1
    #find corners:
    for ccx,ccy in [(0,0),(0,1),(1,0),(1,1)]:
        tx=x+ccx
        ty=y+ccy
        neighs=0    
        nwl=w+2
        nwh=0
        nhl=h+2
        nhh=0
        for cx,cy in [(-1,-1),(-1,0),(0,0),(0,-1)]:
            if inp[ty+cy][tx+cx]==type and ids[ty+cy][tx+cx]==id:
                neighs+=1
                if tx+cx>nwh:
                    nwh=tx+cx
                if tx+cx<nwl:
                    nwl=tx+cx
                if ty+cy>nhh:
                    nhh=ty+cy
                if ty+cy<nhl:
                    nhl=ty+cy
        nw=nwh-nwl
        nh=nhh-nhl
        if neighs==1:
            corners[(tx,ty)]=1
        elif neighs==2:
            if nw>0 and nh>0:
                corners[(tx,ty)]=2
        elif neighs==3:
            corners[(tx,ty)]=1
        else:
            corners.pop((tx,ty),None) #remove if exists
            
    return area,peri,corners

id=0
for y in range(h):
    for x in range(w):
        if visited[y+1][x+1] != " ":
            a,p,c=findarea(inp[y+1][x+1],x+1,y+1,id)
            p1+=a*p
            p2+=a*sum(list(c.values()))
            id+=1

#printmap(inp)
#printmap(visited)
#printmap(ids)
print("1:",p1)
print("2:",p2)
