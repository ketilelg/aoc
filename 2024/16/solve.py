import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    maze = list(map(list,f.read().strip().split("\n")))

sys. setrecursionlimit(20000)

p1=0
p2=0

h=len(maze)
w=len(maze[0])
p1=maxcost=h*w*1000

def printmap(m):
    for l in m:
        for c in l:
            print(c,end="")
        print("")

startx=starty=goalx=goaly=0
visited = [[False]*w for i in range(h)]
costs = [[maxcost]*w for i in range(h)]

for y in range(w):
    for x in range(h):
        if(maze[y][x]=="S"):
            startx=x
            starty=y
        elif(maze[y][x]=="E"):
            goaly=y
            goalx=x
        elif maze[y][x]=="#":
            visited[y][x]=True

dir=">"
dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}

rsets=[]

def mazerun(x,y,dir,score,path):
#    print("mr",x,y,dir,score)
    global p1,maxcost,visited
#    if maze[y][x]=="E":
#        print("end: ",score)
#        return
    for d in "<^>v":
        sc=0
        if costs[y][x]>score:
            costs[y][x]=score
        nx=x+dv[d][0]
        ny=y+dv[d][1]
        if d != dir:
            sc+=1000
        if not visited[ny][nx] and maze[ny][nx]!="E" and costs[ny][nx] >= score+sc:
            visited[ny][nx]=True
#            maze[ny][nx]=d
            mazerun(nx,ny,d,score+sc+1,path|{(nx,ny)})
            visited[ny][nx]=False
#            maze[ny][nx]="."
        if maze[ny][nx]=="E":
            print("end: ",score+1,len(path),path)
            if score+1<p1:
                p1=score+1
#            printmap(maze)
            rsets.append((score+1,path.copy()))
            return

printmap(maze)
#printmap(visited)
print("gg",startx,starty,goalx,goaly)

mazerun(startx,starty,">",0,{(startx,starty)})


print("sdfsdf",len(rsets))

seats=set()
for rs in rsets:
    if rs[0]==p1:
        seats=seats|rs[1]
print("1:",p1)
print("2:",len(seats))
# 540 too low
# 644 too low
