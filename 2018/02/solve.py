import sys
from collections import defaultdict
from itertools import combinations

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

twos=threes=0
for l in inp:
    nnms=defaultdict(str)
    for c in l:
        nnms[l.count(c)]=c
    if nnms[2]:
        twos+=1
    if nnms[3]:
        threes+=1
print("1:",twos*threes)

for a,b in combinations(inp,2):
    neq=0
    res=""
    for i,c in enumerate(a):
        if c==b[i]:
            neq+=1
            res+=c
    print("abab",a,b,neq,res)
    if neq==len(a)-1:
        p2=res

print("2:",p2)
