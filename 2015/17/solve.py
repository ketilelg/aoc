import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split("\n")))

p1=p2=0

# inp.sort()
#print("ii",inp,len(inp),bin(2**len(inp)-1))

counts=defaultdict(int)
for i in range(2**len(inp),2**(len(inp)+1)):
    s=0
    b=bin(i)[3:]
    ps=""
    for j,d in enumerate(b):
        if d=="1":
            s+=inp[j]
            ps+=" "+str(inp[j])
    if s==150:
        print("bb",b, ps)
        p1+=1
        counts[b.count("1")]+=1
p2=counts[min(counts.keys())]
print("1:",p1)
print("2:",p2)
