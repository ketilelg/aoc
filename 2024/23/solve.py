import sys
from functools import cache
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) > 1) else 'input') as f:
    inp = f.read().strip().split("\n")
            

p1=p2=0

conns=defaultdict(tuple)

for l in inp:
    l,r=l.split("-")
    conns[l] += (r,)
    conns[r] += (l,)

groups=set()

@cache
def findset(iset,cset):
    # given set of computers cset, grow it by recursion
    # startinput: cset: set of all neighs for iset (starts with just one). iset: verified set. 
#    print("fset",iset," -- ",cset)
    rset=set()
#    for cc in iset:
    for ccc in cset:
        if not ccc in iset and len(set(iset) & set(conns[ccc]))==len(iset):
            rset=findset(tuple(set(iset) | {ccc}),tuple(set(cset)-{ccc}))
#    print("fse",rset,iset,cset)
    if len(rset) > len(iset):
        return(rset)
    else:
        return(iset)

for c in conns:
    print("--",c,conns[c])
    ll=list(findset((c,),conns[c]))
    ll.sort()
    groups.add(",".join(ll))
    print("qqq",ll)


longest=0
for gg in groups:
    if len(gg)==8 and (gg[0]=="t" or gg[3]=="t" or gg[6]=="t"):
        p1+=1
    if len(gg)>longest:
        p2=gg
        longest=len(gg)

print("1:",p1)
print("2:",p2)
