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
    #find best path
    global p1
    dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}
#    print("mr",score*" ",x,y,score)
    maze[y][x]=score
#    if x==w+1 and y==h+1:
#        return True
    found=False
    score+=1
    for d in dv:
        nx=x+dv[d][0]
        ny=y+dv[d][1]
        if maze[ny][nx]>=0 and score < maze[ny][nx]:
            found = found or mazerun(maze,nx,ny,score)

    return found

def dmazerun(maze,sx,sy,tx,ty):
    #find best path, dijstra?
    global p1
    dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}
#    print("mr",score*" ",x,y,score)
    maze[y][x]=score
#    if x==w+1 and y==h+1:
#        return True
    found=False
    score+=1
    for d in dv:
        nx=x+dv[d][0]
        ny=y+dv[d][1]
        if maze[ny][nx]>=0 and score < maze[ny][nx]:
            found = found or mazerun(maze,nx,ny,score)

    return found


def mazerun2(x,y,score):
    #find A path, nevermind cost
    global p1,maze
    dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}0
#    print("mr",score*" ",x,y,score)
    maze[y][x]=score
    if x==w and y==h:
        return True
    found=False
    score+=1
    for d in dv:
        nx=x+dv[d][0]
        ny=y+dv[d][1]
        if maze[ny][nx]==999999:
            found = found or mazerun2(nx,ny,score)

    return found


for i in range(runl):
    x=memfaults[i][0]
    y=memfaults[i][1]
    maze[y][x]=-1

#mazerun(maze,1,1,0)
p1=maze[w][h]

lowsearch=runl+1
highsearch=len(memfaults)-1
while lowsearch<highsearch:
    runl=int((highsearch+lowsearch)/2)
    # optimize by binary search..
    maze=[[-1] + ([999999] * w) + [-1] for i in range(h)]
    maze.append([-1]*(w+2))
    maze.insert(0,[-1]*(w+2))
    for i in range(runl):
        x=memfaults[i][0]
        y=memfaults[i][1]
        maze[y][x]=-1
    if mazerun2(1,1,0):
        lowsearch=runl+1
    else:
        highsearch=runl-1
    print("dsf",maze[h][w],i,memfaults[i],lowsearch,highsearch)

p2=str(memfaults[lowsearch][0])+","+str(memfaults[lowsearch][1])

print("1:",p1)
print("2:",p2)



