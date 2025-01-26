import sys
import re
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    ii,molecule = f.read().strip().split("\n\n")

rules=[]
for rule in ii.split("\n"):
    l,r=rule.split(" => ")
    rules.append((l,r))

# restr="|".join(rules)

# print("rr",restr,rules)
p1=p2=0

newm=set()

for rr in rules:
    r,l=rr
    print("rule",r,l)
    for i in re.finditer(r,molecule):
        s,e=i.span()
        print("i",molecule[:s]+l+molecule[e:])
        newm.add(molecule[:s]+l+molecule[e:])

print("1:",len(newm)) #615 too high 


print("2:",p2)
