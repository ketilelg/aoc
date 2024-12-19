import sys
from functools import cache

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    f1,f2 = f.read().strip().split("\n\n")

towels=list(f1.split(", "))
designs=f2.split("\n")

p1=0
p2=0

@cache
def designok(design,pos):
#    print("do"," "*pos,design,pos)

    r=0
    for t in towels:
#        print("ddo"," "*pos,t,pos,design[pos:pos+len(t)])
        if t==design[pos:pos+len(t)]:
#            print("phit",pos)
            if pos+len(t)==len(design):
                print("end",design)
                r += 1
            elif pos+len(t)>len(design):
                r += 0
            else:
#                print("no",pos)
                r = r + designok(design,pos+len(t))
    return r

print("tt,",towels,designs)
towels.sort(key=len)
towels.reverse()
print("tt,",towels,designs)


for d in designs:
    r=designok(d,0)
    if r>0:
        p1+=1
    p2+=r
    print("d",r,d)

print("1:",p1)
print("2:",p2)
# 248473060446142 too low
