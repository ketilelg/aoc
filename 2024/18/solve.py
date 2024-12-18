import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(f.read().strip().split("\n"))

if len(sys.argv) == 2:
    runl=12
else:
    runl=1024

sys.setrecursionlimit(20000)

p1=0
p2=0

minx=miny=100000000
maxx=maxy=0
memfaults=[]

for l in inp:
    x,y=int(l.split(",")[0]),int(l.split(",")[1])
    memfaults.append([x+1,y+1])
    if x > maxx:
        maxx=x
    if x < minx:
        minx=x
    if y > maxy:
        maxy=y
    if y < miny: 
        miny=y

w=(maxx-minx)+1
h=(maxy-miny)+1

maze=[[-1] + ([999999] * w) + [-1] for i in range(h)]
maze.append([-1]*(w+2))
maze.insert(0,[-1]*(w+2))

def printmap(m):
    print("map:")
    for l in m:
        for c in l:
            print("|%6d"%c,end="")
        print("<")


def mazerun(maze,x,y,score):
    global p1
    dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}
#    print("mr",score,len(path))
    if x==w+1 and y==h+1:
        return True
    found=False
    maze[y][x]=score
    score+=1
    for d in dv:
        nx=x+dv[d][0]
        ny=y+dv[d][1]
        if maze[ny][nx]>=0 and score < maze[ny][nx]:
            found = found or mazerun(maze,nx,ny,score)

    return found

print("mm",minx,maxx,miny,maxy,memfaults)


for i in range(runl):
    x=memfaults[i][0]
    y=memfaults[i][1]
    maze[y][x]=-1

printmap(maze)

mazerun(maze,1,1,0)

print("1:",maze[w][h],runl)
printmap(maze)
solfound=True
while solfound:
    maze=[[-1] + ([999999] * w) + [-1] for i in range(h)]
    maze.append([-1]*(w+2))
    maze.insert(0,[-1]*(w+2))
    runl+=1
    for i in range(runl):
        x=memfaults[i][0]
        y=memfaults[i][1]
        maze[y][x]=-1
    solfound=mazerun(maze,1,1,0)
    solfound=maze[h][w]<999999
#    printmap(maze)
    print("dsf",w,h,maze[h][w],solfound,i,memfaults[i-1])

# 10,70 wrong (11,71)
# 35,13 wrong (36,14)
# dsf 71 71 302 True 1220 [25, 36] - fortsett fra 1219, elns.



