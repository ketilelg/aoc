import sys
import copy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(list,f.read().strip().split("\n")))

p1=p2=0

visited=copy.deepcopy(inp)
w=len(inp)
h=len(inp[0])

def printmap(m):
    for y in range(h):
        for x in range(w):
            print(m[y][x],end="")
        print("")

def findarea(type,x,y,dx,dy):
    area=1
    peri=0
    sides=0
    visited[y][x]=" "
    for dir in [(-1,0),(0,-1),(1,0),(0,1)]:
        nx=x+dir[0]
        ny=y+dir[1]
        if(0<=nx<w and 0<=ny<h and inp[ny][nx]==type and visited[ny][nx] != " "):

            a,p,s=findarea(type,nx,ny,dir[0],dir[1])
            area+=a
            peri+=p
            sides+=s
        elif nx < 0 or nx >= w or ny < 0 or ny >= w or inp[ny][nx]!=type:
            peri+=1
            if dx!=dir[0] or dy!=dir[1]:
                sides+=1

#        print("fa",type,x,y,nx,ny,dx,dy,dir,area,peri,sides)
    return area,peri,sides



for y in range(h):
    for x in range(w):
        if visited[y][x] != " ":
            a,p,s=findarea(inp[y][x],x,y,0,0)
#            printmap(visited)
            print("ff",a,p,s)
            p1+=a*p
            p2+=a*s

print("1:",p1)
print("2:",p2)
