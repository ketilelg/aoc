import sys
import re
with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


for b in inp:
    f=re.search(r"^(\D+) (\d+),(\d+) through (\d+),(\d+)",b)
    print("ff",f)


print("1:",p1)
print("2:",p2)
