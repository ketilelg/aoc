import sys
import copy
from collections import defaultdict


with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(list,f.read().strip().split("\n")))

p1=p2=0

w=len(inp)
h=len(inp[0])

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

def findarea(type,x,y,dx,dy,id):
    area=1
    peri=0
    sides=0
    neighs=0
    corners={}
#    corners=set()
    neigw=neigh=0
    visited[y][x]=" "
    ids[y][x]=id
#    print("fai",type,x,y)
    for dir in [(-1,0),(0,-1),(1,0),(0,1)]:
        nx=x+dir[0]
        ny=y+dir[1]
#        if(0<=nx<w and 0<=ny<h and inp[ny][nx]==type and visited[ny][nx] != " "):
        if(inp[ny][nx]==type and visited[ny][nx] != " "):
            a,p,s,c=findarea(type,nx,ny,dir[0],dir[1],id)
            area+=a
            peri+=p
            sides+=s
            corners.update(c)
#            corners=corners.union(c)
            
#        elif nx < 0 or nx >= w or ny < 0 or ny >= w or inp[ny][nx]!=type:
        elif inp[ny][nx]!=type:
            peri+=1

#        if  (0<=nx<w and 0<=ny<h and inp[ny][nx]!=type):
#            corners.add((nx,ny))

    #         neigw+=abs(dir[0])
    #         neigh+=abs(dir[1])
    #         neighs+=1
    for ccx,ccy in [(0,0),(0,1),(1,0),(1,1)]:
        tx=x+ccx
        ty=y+ccy
        neighs=0    
        nwl=w+2
        nwh=0
        nhl=h+2
        nhh=0
        print("fff",tx,ty)
        for cx,cy in [(-1,-1),(-1,0),(0,0),(0,-1)]:
#            print("fnn",tx,ty,cx,cy)
#            print("fn",cx,",",cy,"-",inp[ty+cy][tx+cx],"=",type,"|",end="")
            if inp[ty+cy][tx+cx]==type and ids[ty+cy][tx+cx]==id:
#                print("ttthit")
                neighs+=1
                if tx+cx>nwh:
                    nwh=tx+cx
                if tx+cx<nwl:
                    nwl=tx+cx
                if ty+cy>nhh:
                    nhh=ty+cy
                if ty+cy<nhl:
                    nhl=ty+cy

#                nw+=abs(cx)
#                nh+=abs(cy)
#            print("fnn2",tx,ty,nwl,nwh,nhl,nhh,cx,cy,neighs)

        nw=nwh-nwl
        nh=nhh-nhl

        if neighs==0:
            # corners=4
            print("wut?")
        elif neighs==1:
            corners[(tx,ty)]=1
        elif neighs==2:
            print("22",nw,nh,tx,ty)
            if nw>0 and nh>0:
                corners[(tx,ty)]=2
                print("hh",corners)
        elif neighs==3:
            corners[(tx,ty)]=1
    

    print("fa",type,x,y,nx,ny,dx,dy,dir,area,peri,sides,corners,neighs)
    return area,peri,sides,corners



def findsides(type,sx,sy,x,y,dirx,diry):
    print("fs",type,x,y,dirx,diry)
    visited2[y][x]=" "
    sides=0
    vl=defaultdict(dict)
    hl=defaultdict(dict)
    for dir in [(-1,0),(0,-1),(1,0),(0,1)]:
        nx=x+dir[0]
        ny=y+dir[1]
        if(0<=nx<w and 0<=ny<h and inp[ny][nx]==type and visited2[ny][nx] != " "):
            s,hh,vv=findsides(type,sx,sy,nx,ny,dir[0],dir[1])
            sides+=s
            hl.update(hh)
            vl.update(vv)
        print("nn",nx,ny)
        if dir[0]==-1:
            if nx < 0 or inp[nx][ny] != type:
                hl[x]=y
        elif nx >= w or inp[nx][ny] != type:
            hl[nx]=ny 
        elif ny < 0 or (nx < w and ny < h and inp[nx][ny]) != type:
            vl[y]=nx 
        elif ny >= h or inp[nx][ny] != type:
            vl[ny]=nx

    print("fsr",type,x,y,sides,list(hl),list(vl))        
    return(sides,hl,vl)

id=0
for y in range(h):
    for x in range(w):
        if visited[y+1][x+1] != " ":
            a,p,s,c=findarea(inp[y+1][x+1],x+1,y+1,0,0,id)
#            s,hl,vl=findsides(inp[y][x],x,y,x,y,0,0)
#            printmap(visited)
            sides=sum(list(c.values()))
            print("FF",a,p,sides)
            #,c,list(c.values()))
            p1+=a*p
            p2+=a*sides
            id+=1

printmap(inp)
#printmap(visited)
printmap(ids)
print("1:",p1)
print("2:",p2)
# 922532 too high. 
# 922141 too high. 