import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    stories = [list(map(int,s.split())) for s in f.read().strip().split("\n")]

    
def extend(ii):
    s=ii
    if(sum(s)==0):
        return s+[0,0]
    else:
        ns=[(s[n+1]-s[n]) for n,v in enumerate(s[1:])]
        nns=extend(ns)
        s.append(s[-1]+nns[-1])
        s.insert(0,(s[0]-nns[0]))

        return s
    
for st in stories:
    extend(st)
    s2+=st[0]
    s1+=st[-1]

print("1:", s1)
    
print("2:", s2)

