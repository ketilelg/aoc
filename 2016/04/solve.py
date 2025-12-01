import sys
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


def rotc(c,rot):
    return(chr((ord(c) - ord("a") + int(rot))%26 + ord("a")))

for k in inp:
    nc=defaultdict(int)
    parts=k.split("-")
#    print("pp",parts)
    for p in parts[:-1]:
#        print("p",p)
        for c in list(p):
            nc[c]+=1
    id,cksum=parts[-1][:-1].split("[")
    sli=sorted(nc.items(), key=lambda item: item[0])
#    print("nc",id,cksum,sli)
    sli.sort(key = lambda x: x[1],reverse=True)
#    print("nnc",sli)
    cs="".join([x[0] for x in sli])
#    print("cs",cs)
    if (cksum == cs[:5]):
#        print("eq")
        p1+=int(id)
#    print("sdf","".join(sorted("".join(parts[:-1]))))

    ro=""
    for c in k:
        print("c",c,id)
        ro+=rotc(c,id)
    print("ro",ro,id)

print("1:",p1)
print("2:",p2)
