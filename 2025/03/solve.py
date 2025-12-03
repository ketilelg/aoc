import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

for l in inp:
    sifre=list(map(int,list(l)))
    s1=max(sifre[:-1])
    s1pos=sifre.index(s1)
    s2=max(sifre[s1pos+1:])
    p1+=(s1*10)+s2

    p2v=0    
    spos=0
    for i in range(11,-1,-1):
        epos=len(sifre)-i
        sif=(max(sifre[spos:epos]))
        p2v*=10
        p2v+=sif
        spos=sifre[spos:].index(sif)+1+spos
    p2+=p2v

print("1:",p1)
print("2:",p2)
