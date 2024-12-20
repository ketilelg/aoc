import sys

sys.setrecursionlimit(20000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    maze = list(map(list,f.read().strip().split("\n")))

p1=0
p2=0

#xmap=copy.deepcopy(map)
h=len(maze)
w=len(maze[0])


p1=0
p2=0

minx=miny=100000000
maxx=maxy=0
memfaults=[]


def printmap(m):
    print("map:")
    for l in m:
        for c in l:
#            print("|%6d"%c,end="")
            print(c,end="")
        print("<")

startx=starty=goalx=goaly=0
for y in range(h):
    for x in range(w):
        if maze[y][x]=="S":
            startx=x
            starty=y
        elif maze[y][x]=="E":
            goalx=x
            goaly=y


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


def mazerun2(maze,x,y,gx,gy):
    dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}
#    print("mr",score*" ",x,y,score)
    pq=[(0,(x,y))]
    while pq:
        printmap(maze)
        sc,cur=pq.pop(0)
        for d in dv:
            nx=cur[0]+dv[d][0]
            ny=cur[1]+dv[d][1]
            if maze[ny][nx] in ".E":
                pq.append((sc+1,(nx,ny)))
                maze[cur[1]][cur[0]]=d
                if nx==gx and ny==gy:
                    return sc

printmap(maze)
print("sx",startx,starty,goalx,goaly)

print("mm",mazerun2(maze,startx,starty,goalx,goaly))

printmap(maze)
print("1:",p1)
print("2:",p2)



