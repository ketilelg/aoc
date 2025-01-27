import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    ii,molecule = f.read().strip().split("\n\n")

rules=[]
for rule in ii.split("\n"):
    l,r=rule.split(" => ")
    rules.append((l,r))

p1=p2=0

newm=set()

for rr in rules:
    r,l=rr
    for i in re.finditer(r,molecule):
        s,e=i.span()
        newm.add(molecule[:s]+l+molecule[e:])

print("1:",len(newm)) 

while molecule != "e":
    for l,r in rules:
        molecule,nn=re.subn(r,l,molecule)
        p2+=nn

print("2:",p2)
