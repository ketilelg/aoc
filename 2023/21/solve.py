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

mult=11

tmap=[["." for x in range(w*mult)] for y in range(h*mult)]


for x in range(w):
    for y in range(h):
        if(mmap[y][x]=="S"):
           startx=x
           starty=y
        mid=int((mult-1)/2)
        for xm in range(mult):
            for ym in range(mult):
                if((mmap[y][x]!="S") or (xm==mid and ym==mid)):
                    tmap[y+(h*ym)][x+(w*xm)]=mmap[y][x]
                else:
                    tmap[y+(h*ym)][x+(w*xm)]="."

                
                
printm(tmap)

print(startx,starty)


def runit(mmap):
    bmap=copy.deepcopy(mmap)
    w=len(mmap[0])
    h=len(mmap)

    #blank copy
    def step(smap,gen,sgen):
        global s1
        nmap=copy.deepcopy(bmap)
        print("startstep",gen)
        #    printm(smap)
        #    printm(nmap)
        nplot=0
        if(gen>0):
            for y in range(h):
                for x in range(w):
                    if(smap[y][x]=="O" or (sgen==gen and smap[y][x]=="S")):
                        #                    print("is",x,y,smap[y][x])
                        for dx,dy in (-1,0),(0,-1),(1,0),(0,1):
                            if((0 <= y+dy < h) and (0 <= x+dx < w) and
                               (nmap[y+dy][x+dx] != "#")):
#                            print("pp",x,y,dx,dy,nmap[y+dy][x+dx])
                                if(nmap[y+dy][x+dx] != "O"):
                                    nplot+=1
                                    nmap[y+dy][x+dx] = "O"
            print("step",gen,nplot)
            s1=nplot
            printm(nmap)
            step(nmap,gen-1,sgen)
    step(bmap,1000,1000)
            
runit (tmap)        

print("1:", s1)


print("2:", s2)

