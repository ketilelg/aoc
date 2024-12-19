import sys
from functools import cache

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    f1,f2 = f.read().strip().split("\n\n")

towels=f1.split(", ")
designs=f2.split("\n")

p1=0
p2=0

@cache
def designok(design,pos):
    r=0
    for t in towels:
        if t==design[pos:pos+len(t)]:
            if pos+len(t)==len(design):
                r += 1 #result!
            elif pos+len(t)<=len(design):
                r = r + designok(design,pos+len(t))
    return r

for d in designs:
    r=designok(d,0)
    if r>0:
        p1+=1
    p2+=r

print("1:",p1)
print("2:",p2)
