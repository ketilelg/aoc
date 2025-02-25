import sys
import copy

sys.setrecursionlimit(20000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    maze = list(map(list,f.read().strip().split("\n")))

p1=0
p2=0

h=len(maze)
w=len(maze[0])

p1=0
p2=0


def printmap(m):
#    print("map:")
    for l in m:
        for c in l:
#            print("|%6d"%c,end="")
            print(c,end="")
        print("<")


def printdmap(m):
#    print("map:")
    for l in m:
        for c in l:
            print("|%6d"%c,end="")
#            print(c,end="")
        print("|")

startx=starty=goalx=goaly=0
for y in range(h):
    for x in range(w):
        if maze[y][x]=="S":
            startx=x
            starty=y
        elif maze[y][x]=="E":
            goalx=x
            goaly=y

dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}

dmaze=[[999999]*w for _ in range(h)]

def mazerun(maze,x,y,gx,gy):
    pq=[(0,(x,y))]
    path=[]
    while pq:
        sc,cur=pq.pop(0)
        for d in dv:
            nx=cur[0]+dv[d][0]
            ny=cur[1]+dv[d][1]
            if maze[ny][nx] in ".E":
                pq.append((sc+1,(nx,ny)))
                dmaze[cur[1]][cur[0]]=sc
                maze[cur[1]][cur[0]]=d
                path.append((d,cur[0],cur[1]))
                if nx==gx and ny==gy:
                    dmaze[ny][nx]=sc+1
                    return path,sc




omaze=copy.deepcopy(maze)
gains={}
path,score=mazerun(maze,startx,starty,goalx,goaly)

#printdmap(dmaze)

l=0
for p in path:
    x=p[1]
    y=p[2]
    thiscost=dmaze[y][x]
#    print("p",x,y)
#    for dist in range(1,min(20,abs(goalx-x)+abs(goaly-y)+2)):
    for dist in range(1,20):
        testpoints=set()
        for d in dv:
#            print("  fdsv",d)
            dx=dv[d][0]
            dy=dv[d][1]
            nx=x+dx
            ny=y+dy
            if True: # maze[ny][nx]=="#" or dmaze[ny][nx]>thiscost:
                for i in range(1,dist+1):
                    if d in "^v":
                        testpoints.add((nx+((dist-i)),ny+(i*dy)))
                        testpoints.add((nx-((dist-i)),ny+(i*dy)))
                    else:
                        testpoints.add((nx+(i*dx),ny+((dist-i))))
                        testpoints.add((nx+(i*dx),ny-((dist-i))))
        for tp in testpoints:
            ey=tp[1]
            ex=tp[0]
            if 0<ex<w and 0<ey<h and thiscost+dist+1 < dmaze[ey][ex] < 999999:
                gain=dmaze[ey][ex]-thiscost-dist-1
                if not gain in gains:
                    gains[gain]=1
                else:
                    gains[gain]+=1
                if gain >= 100:
                    if dist==1:
                        p1+=1
                    p2+=1
    l+=1

print("1:",p1)
print("2:",p2)



