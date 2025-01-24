import sys
from collections import defaultdict
from copy import deepcopy
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(list,f.read().strip().split("\n")))

def printmap(m):
    for l in m:
        for c in l:
            print(c,end="")
        print("")


def ngen(m):
    w=len(m[0])
    h=len(m)
    new=deepcopy(m)
    for x in range(w):
        for y in range(h):
            nn=0
            for xx in range((max(0,x-1)),min(w,x+2)):
                for yy in range((max(0,y-1)),min(h,y+2)):
                    if m[yy][xx]=="#":
                        nn+=1
#                    print("xy",x,y,xx,yy,nn)
            if (m[y][x]=="." and nn==3) or (m[y][x]=="#" and (nn==3 or nn==4)):
                new[y][x]="#"
            else:
                new[y][x]="."
#            print(nn,end="")
#        print()
    return new
                            
p1=p2=0

p1inp=deepcopy(inp)
for i in range(100):
    p1inp=ngen(p1inp)
#    printmap(inp)

for i in range(100):
    inp[0][0]="#"
    inp[-1][0]="#"
    inp[-1][-1]="#"
    inp[0][-1]="#"
    inp=ngen(inp)

inp[0][0]="#"
inp[-1][0]="#"
inp[-1][-1]="#"
inp[0][-1]="#"

def countit(inp):
    r=0
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x]=="#":
                r+=1
    return r
print("1:",countit(p1inp)) 
print("2:",countit(inp))
