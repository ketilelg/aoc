import sys
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=""
p2=""

stats=[]
for i in range(len(inp[0])):
    stats.append(defaultdict(int))

for k in inp:
    for pos,char in enumerate(k):
        stats[pos][char]+=1

print("ss",stats)

for d in stats:
    mi=max(d.items(), key= lambda item: item[1])
    p1+=mi[0]
    mi=min(d.items(), key= lambda item: item[1])
    p2+=mi[0]
print("1:",p1)
print("2:",p2)
