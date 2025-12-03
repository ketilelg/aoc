import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

for l in inp:
    print("l":l)

print("1:",p1)
print("2:",p2)
