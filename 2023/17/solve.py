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
            v=dmap[y][x][0]
            if(v<1000):
                print("%3d " % v,end="")
            else:
                print("    ",end="")
        print()


print("wh",w,h)
    #gitt punkt x,y, se om vi kan prøve å kjøre ut i alle retninger det er mulig
    #d=direction vi kom fra, l=lengen av bevegelse i denne retningen
    #hl=heatloss
def find(x,y,d,l,hl):
    global mhl,h,w
    print("f",x,y,d,l,hl,mhl,w,h)
    printvm()

    if(not visited[y][x]):
        visited[y][x]=True
        hl+=mmap[y][x]
#        dmap[y][x]=(hl," ",4)
#        if(hl >= mhl):
#            visited[y][x]=False
#            print("too long",x,y,hl)
#            return(hl)
        if((x==w-1) and (y==h-1)):
#            printv(visited)
            print("ee",x,y,h,hl,mhl)
#            if(hl < mhl):
#                mhl=hl
#            visited[y][x]=False
#            return(mhl)
#            res=w*h*10
        neig=[] #list of dists of unvis
#        if(((x<(w-1)) and (not visited[y][x+1]) and ((d!=">") or (l<maxlen)))):
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx=x+dx
            ny=y+dy

                
            if((0 <= nx <= (w-1)) and (0 <= ny <= (h-1)) and (not visited[y+dy][x+dx])):

                tv=hl+mmap[ny][nx]
                if(tv < dmap[ny][nx][0]):
                    dmap[ny][nx]=(tv," ",4)
                    tup=(tv,dx,dy)
                    neig.append(tup)

        if(neig):
            print("fr",x,y,hl,neig)
            neig.sort()
            for best in neig:
#                best=neig[0]
                dx=best[1]
                dy=best[2]
                r=find(x+dx,y+dy," ",1,hl)
#        visited[y][x]=False
#        return(res)
    else:
        print("wtf=??")
        return(mhl)

print("ff",find(0,0,">",1,0))

printm(dmap)
printv(visited)

print("1:", s1)
# 1157 too high

print("2:", int(s2))

