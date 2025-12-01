import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

pos=50
for l in inp:
    v=int(l[1:])
    if l[0]=="L":
        pos-=v
    else:
        pos+=v

    p2+=abs(int(pos/100))
    if pos<=0 and pos!=-v:
        p2+=1

    pos=pos%100
    if pos==0:
        p1+=1

print("1:",p1)
print("2:",p2)
