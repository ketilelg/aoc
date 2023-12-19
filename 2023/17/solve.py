import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    mmap =  [list(map(int,list(s))) for s in f.read().strip().split("\n")]

h=len(mmap)
w=len(mmap[0])

def printm(m):
    for l in m:
        for c in l:
            print(c," ",end="")
        print()

def printv(m):
#    print("\033c")
    for l in m:
        for c in l:
            if(c):
                print("X",end="")
            else:
                print(".",end="")
        print()

        
        
printm(mmap)
print("wh",w,h)
mhl = w * h * 10

dmap=[[(mhl," ",4) for x in range(w)] for y in range(h)]
dmap[0][0]=(mmap[0][0]," ",0) #cost, dir into, count of dir

visited=[[False for x in range(w)] for y in range(h)]
maxlen=mhl #normally 3, but..

def printvm():
#    print("\033c")
    for y in range(h):
        for x in range(w):
            c=visited[y][x]
            if(c):
                print("X",end="")
            else:
                print(".",end="")
            print("%3d" % dmap[y][x][2],end="")
            print(dmap[y][x][1],end="")
            v=dmap[y][x][0]
            if(v<1000):
                print("%3d " % v,end="")
            else:
                print("    ",end="")
        print()


    #en variant av Dijkstra
    #d=direction vi kom fra, l=lengen av bevegelse i denne retningen
    #hl=heatloss
def find(x,y,d,l,hl):
    global mhl,h,w
    print("f",x,y,d,l,hl)
    printvm()

    if(not visited[y][x]):
        visited[y][x]=True
        hl=dmap[y][x][0]
        if((x==w-1) and (y==h-1)):
            print("ee",x,y,h,hl,mhl)
            printvm()
            return(hl)
        for dx,dy,dir in [(1,0,">"),(0,1,"v"),(-1,0,"<"),(0,-1,"^")]:
            nx=x+dx
            ny=y+dy

            if((0 <= nx <= (w-1)) and (0 <= ny <= (h-1)) and (not visited[y+dy][x+dx])):

                tv=hl+mmap[ny][nx]
                if(tv < dmap[ny][nx][0]):
                    dmap[ny][nx]=(tv,dir,1 if dir != dmap[y][x][1] else dmap[y][x][2]+1)
            bx=0
            by=0
            bd=mhl
        #find lowest unvisited:
        for xx in range(w):
            for yy in range(h):
                if(not visited[yy][xx] and (dmap[yy][xx][0] < bd)):
                    bd=dmap[yy][xx][0]
                    bx=xx
                    by=yy
        return find(bx,by," ",1,hl)
    else:
        print("wtf=??")
        return(mhl)

print("ff",find(0,0,">",1,0))

#printm(dmap)
#printv(visited)

print("1:", s1)
# 1157 too high

print("2:", int(s2))

