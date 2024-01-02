import math
import copy
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    mmap =  f.read().strip().split("\n")

w=len(mmap[0])
h=len(mmap)



def printm(m):
    for l in m:
        for c in l:
            print(c,end="")
        print()
        

visited=[[False]*w for s in range(h)]

def printv():
    for y,l in enumerate(mmap):
        for x,c in enumerate(l):
            if(visited[y][x]):
                print("O",end="")
            else:
                print(c,end="")
        print()
# printm(mmap)

maxlen=0
ncalls=0
def solve(x,y,finalx,finaly,length):
    global maxlen
#    print("solve",x,y,finalx,finaly,length)
    if(length>maxlen):
        maxlen=length
        print("maxlen",maxlen)
    visited[y][x]=True
    if(x==finalx and y==finaly):
        visited[y][x]=False
        return 0
    #se i alle retninger..
    retv=reth=reto=retn=-10000
    if((x>0)   and ((mmap[y][x-1] in ".<")) and not visited[y][x-1]):
        retv=solve(x-1,y,finalx,finaly,length+1)
    if((x<w-1) and ((mmap[y][x+1] in ".>")) and not visited[y][x+1]):
        reth=solve(x+1,y,finalx,finaly,length+1)
    if((y>0)   and ((mmap[y-1][x] in ".^")) and not visited[y-1][x]):
        reto=solve(x,y-1,finalx,finaly,length+1)
    if((y<h-1) and ((mmap[y+1][x] in ".v")) and not visited[y+1][x]):
        retn=solve(x,y+1,finalx,finaly,length+1)
    visited[y][x]=False
    maxl=max(retv,reth,reto,retn)+1
#    print("solve end",maxl)
#    printv()
    return(maxl)

def solve2(x,y,finalx,finaly,length):
    global maxlen,ncalls
#    print("solve2",x,y,finalx,finaly,length)

    visited[y][x]=True
    ncalls+=1
    if(x==finalx and y==finaly):
        visited[y][x]=False
        print("visit",length,ncalls)
        if(length>maxlen):
            maxlen=length
            print("maxlen2",maxlen)
        return 1
    #se i alle retninger..
    retv=reth=reto=retn=-10000
    if((x>0)   and ((mmap[y][x-1] != "#")) and not visited[y][x-1]  and not ((y==h-2) and (x<finalx))):
        retv=solve2(x-1,y,finalx,finaly,length+1)
    if((x<w-1) and ((mmap[y][x+1] != "#")) and not visited[y][x+1]):
        reth=solve2(x+1,y,finalx,finaly,length+1)
    if((y>0)   and ((mmap[y-1][x] != "#")) and not visited[y-1][x] and not ((x==w-2) or (x==1))):
        reto=solve2(x,y-1,finalx,finaly,length+1)
    if((y<h-1) and ((mmap[y+1][x] != "#")) and not visited[y+1][x]):
        retn=solve2(x,y+1,finalx,finaly,length+1)
    visited[y][x]=False
    maxl=max(retv,reth,reto,retn)+1
#    print("solve2 end",maxl)
#    printv()
#    printv()
    return(maxl)


s1=solve(mmap[0].find("."),0,mmap[-1].find("."),h-1,0)   

print("1:", s1,maxlen)

maxlen=0
s2=solve2(mmap[0].find("."),0,mmap[-1].find("."),h-1,0)   
#s2=maxlen
printv()
print("2:", s2,maxlen+1)
# 6587 too high
# 6586 correct
# output:
# 2: 6774 6587

