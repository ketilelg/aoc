import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

vars={}

def findvar(vars,v):
    if v.isdigit():
        return(int(v))
    d=vars[v]
    if type(d) is int:
        return d
    if d.count("AND") > 0:
        l,op,r=re.match(r"(\S+)\s+(\S+)\s+(\S+)",d).groups()    
        vars[v]=findvar(vars,l) & findvar(vars,r)
    elif d.count("LSHIFT") > 0:
        l,op,r=re.match(r"(\S+)\s+(\S+)\s+(\S+)",d).groups()    
        vars[v]=findvar(vars,l) << int(r)
    elif d.count("RSHIFT") > 0:
        l,op,r=re.match(r"(\S+)\s+(\S+)\s+(\S+)",d).groups()    
        vars[v]=findvar(vars,l) >> int(r)
    elif d.count("NOT") > 0:
        op,r=re.match(r"(\S+)\s+(\S+)",d).groups()    
        vars[v]=findvar(vars,r) ^ 65535
    elif d.count("OR"):
        l,op,r=re.match(r"(\S+)\s+(\S+)\s+(\S+)",d).groups()    
        vars[v]=findvar(vars,l) | findvar(vars,r)
    elif d in vars:
        vars[v]=findvar(vars,d)
    else:
        vars[v]=int(d)
    return vars[v]

for l in inp:
    l,r=l.split(" -> ")
    vars[r]=l

vars2=vars.copy()

p1=findvar(vars,"a")
print("1:",p1)

vars2["b"]=p1
print("2:",findvar(vars2,"a"))
