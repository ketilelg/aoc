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
            if nn==4 or (m[y][x]=="#" and nn==3):
                new[y][x]="#"
            else:
                new[y][x]="."
    return new
                            
p1=p2=0
w=len(inp[0])
h=len(inp)
print("sdf",w,h,inp)
printmap(inp)
i=ngen(inp)
print("sdfsdf")
printmap(i)
print("1:",p1)
print("2:",p2)
