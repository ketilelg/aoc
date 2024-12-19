import sys
from functools import cache

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n\n")

towels=inp[0].split(", ")
designs=inp[1].split("\n")

p1=0
p2=0

@cache
def designok(design):
    r=0
    for t in towels:
        if design.startswith(t):
            if len(t)==len(design):
                r += 1 #result!
            else:
                r = r + designok(design[len(t):])
    return r

for d in designs:
    r=designok(d)
    if r>0:
        p1+=1
    p2+=r

print("1:",p1)
print("2:",p2)
