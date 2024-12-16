import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    maze = list(map(list,f.read().strip().split("\n")))

sys.setrecursionlimit(20000)

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

def printscore(m):
    for l in m:
        for d in "<^>v":
            print(d," ",end="")
            for c in l:
                print("|%7d"%c[d],end="")
            print("|")
        print("")

startx=starty=goalx=goaly=0

visited = [[False]*w for i in range(h)]
costs = [[{"<":maxcost,"^":maxcost,">":maxcost,"v":maxcost} for j in range(w)] for i in range(h)]

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


altd={"^":"^<>",">":">^v","v":"v<>","<":"<^v"} #straigh ahead first

def mazerun(x,y,dir,score,path):
    global p1,maxcost,visited
#    print("mr",score,len(path))
    found=False
    visited[y][x]=True
    if costs[y][x][dir]>score:
        costs[y][x][dir]=score


    for d in altd[dir]:
        sc=0
        nx=x+dv[d][0]
        ny=y+dv[d][1]
        if d != dir:
            sc=1000
        if maze[ny][nx]=="E":
            print("end: ",score,len(path))
            found=True
            if score<=p1:
                p1=score
                rsets.append((score,path.copy())) #remember this path.
#            for s in path:
#                maze[s[1]][s[0]]="O"
        elif not visited[ny][nx] and maze[ny][nx]!="#" and score+sc < p1 and costs[ny][nx][d] >= score+sc+1:
            found=mazerun(nx,ny,d,score+sc+1,path|{(nx,ny)})
        if not found:
            maze[ny][nx]="#"

    visited[y][x]=False
    return found

mazerun(startx,starty,">",1,{(startx,starty)})

# printscore(costs)

# print("sdfsdf",len(rsets))

seats=set()
for rs in rsets:
    if rs[0]==p1:
#        print("rs",rs[1])
        seats=seats|rs[1]

for s in seats:
    maze[s[1]][s[0]]="O"

printmap(maze)

print("1:",p1)
print("2:",len(seats)+1)
