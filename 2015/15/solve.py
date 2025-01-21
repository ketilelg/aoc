import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


ingr={}
for b in inp:
    name,rest=b.split(":")
    print("rr",re.findall(r"\-?\d+",rest))
    ingr[name]=re.findall(r"\-?\d+",rest)

print("i",ingr)
print("1:",p1) 
print("2:",p2)
