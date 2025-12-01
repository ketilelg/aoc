import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

pos=50
for l in inp:
    v=int(l[1:])
    pp=pos
    if l[0]=="L":
        pos-=v
    else:
        pos+=v

    if(pos>100):
        p2+=abs(int(pos/100))
        if pos%100==0:
            p2-=1
    if pos<0:
        p2+=abs(int(pos/100))
        if pp!=0 and pos%100!=0:
            p2+=1

    pos=pos%100
    if pos==0:
        p1+=1
        p2+=1

print("1:",p1)
print("2:",p2)
