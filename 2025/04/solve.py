import sys
from collections import defaultdict
import re
from copy import deepcopy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    fmap = list(map(list,f.read().strip().split("\n")))

p1=p2=0

h=len(fmap)
w=len(fmap[0])    

def printmap(nmap):
    print("\033[H")
    for l in nmap:
        for c in l:  
            print(c,end="")
        print("")

for x in range(w):
    for y in range(h):
        if fmap[y][x]=="@":
            nneig=0
            for oy in range(-1,2):
                for ox in range(-1,2):
                    if x+ox>=0 and x+ox<w and y+oy>=0 and y+oy<h:
                        if fmap[y+oy][x+ox]=="@":
                            nneig+=1
            if nneig<5:
                p1+=1

np2=1
newmap=deepcopy(fmap)
while np2!=p2:
    np2=p2
    printmap(newmap)
    for x in range(w):
        for y in range(h):
            if fmap[y][x]=="@":
                nneig=0
                for oy in range(-1,2):
                    for ox in range(-1,2):
                        if x+ox>=0 and x+ox<w and y+oy>=0 and y+oy<h:
                            if fmap[y+oy][x+ox]=="@":
                                nneig+=1
                if nneig<5:
                    p2+=1
                    newmap[y][x]="."
    fmap=deepcopy(newmap)

print("1:",p1)
print("2:",p2)
