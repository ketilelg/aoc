import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    mmap =  [list(map(int,list(s))) for s in f.read().strip().split("\n")]

h=len(mmap)
w=len(mmap[0])

def printm(m):
    for l in m:
        for c in l:
            print(c,end="")
        print()

printm(mmap)

maxdist=w*h*10

dmap=[[(maxdist," ",4) for x in range(w)] for y in range(h)]

dmap[0][0]=(mmap[0][0]," ",0) #cost, dir into, count of dir

# lag tabell med avstand fra start, blir vel en revers floddfill??==


maxlen=maxdist #normally 3, but for the sake of an argument..

r=maxdist
change=True
while(change):
    change=False
    s1=r
    for x in range(w):
        for y in range(h):
                ml=dmap[y][x][2] #we want to minimize length of straights
                md=dmap[y][x][1]
                #look left:
                if((x>0) and ((dmap[y][x-1][0]+mmap[y][x]) <= dmap[y][x][0])
                   and ((dmap[y][x-1][1] != ">") or (dmap[y][x-1][2] < maxlen))):
                    ll= dmap[y][x-1][2]+1 if (dmap[y][x-1][1] == ">") else 1
                    if(ll < ml):
                        dmap[y][x]=(dmap[y][x-1][0] + mmap[y][x],">",ll)
                        change=True
                #look up:
                if((y>0) and ((dmap[y-1][x][0]+mmap[y][x]) <= dmap[y][x][0])
                   and ((dmap[y-1][x][1] != "v") or (dmap[y-1][x][2] < maxlen))):
                    ll= dmap[y-1][x][2]+1 if (dmap[y-1][x][1] == "v") else 1
                    if(ll < ml):
                        dmap[y][x]=(dmap[y-1][x][0] + mmap[y][x],"v",ll)
                        change=True
                #look right:
                if((x<w-1) and ((dmap[y][x+1][0]+mmap[y][x]) <= dmap[y][x][0])
                   and ((dmap[y][x+1][1] != "<") or (dmap[y][x+1][2] < maxlen))):
                    ll= dmap[y][x+1][2]+1 if (dmap[y][x+1][1] == "<") else 1
                    if(ll < ml):
                        dmap[y][x]=(dmap[y][x+1][0] + mmap[y][x],"<",ll)
                        change=True
                #look down:
                if((y<h-1) and ((dmap[y+1][x][0]+mmap[y][x]) <= dmap[y][x][0])
                   and ((dmap[y+1][x][1] != "^") or (dmap[y+1][x][2] < maxlen))):
                    ll= dmap[y+1][x][2]+1 if (dmap[y+1][x][1] == "^") else 1
                    if(ll < ml):
                        dmap[y][x]=(dmap[y+1][x][0] + mmap[y][x],"^",ll)
                        change=True
    r=dmap[h-1][w-1][0]
#    printm(dmap)
    print("r",r)





print("1:", s1)
# 1157 too high

print("2:", int(s2))

