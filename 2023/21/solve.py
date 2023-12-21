import math
import copy
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    mmap =  [list(s)for s in f.read().strip().split("\n")]

w=len(mmap[0])
h=len(mmap)

def printm(m):
    for l in m:
        for c in l:
            print(c,end="")
        print()
        
printm(mmap)

for x in range(w):
    for y in range(h):
        if(mmap[y][x]=="S"):
           startx=x
           starty=y

print(startx,starty)

bmap=copy.deepcopy(mmap)
#blank copy
def step(smap,gen):
    nmap=copy.deepcopy(bmap)
    print("startstep",gen)
    printm(smap)

    if(gen>0):
        for y in range(h):
            for x in range(w):
                if(smap[y][x]=="O" or smap[y][x]=="S"):
#                    print("is",x,y,smap[y][x])
                    for dx,dy in (-1,0),(0,-1),(1,0),(0,1):
                        if(nmap[y+dy][x+dx] != "#"):
#                            print("pp",x,y,dx,dy)
                            nmap[y+dy][x+dx] = "O"
        print("step",gen)
        printm(nmap)
        step(copy.deepcopy(nmap),gen-1)
                                
step(mmap,2)        

print("1:", s1)


print("2:", s2)

