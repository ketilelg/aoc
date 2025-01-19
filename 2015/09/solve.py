import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=100000
p2=0

dists={}
towns=set()
for b in inp:
    r,dist=b.split(" = ")
    fr,to=r.split(" to ")
 #   print("sdf",to,fr,dist)
    dists[(fr,to)]=int(dist)
    dists[(to,fr)]=int(dist)
    towns.add(fr)
    towns.add(to)


def distcalc(tset,d,fr):
    global p1,p2
#    print("dc",tset,fr,d)
    if tset:
        for t in tset:
            nd=d
            if fr:
                nd+=dists[(fr,t)]
            ns=tset.copy()
            ns.discard(t)
            distcalc(ns,nd,t)
    else:
        if d<p1:
            p1=d
        if d>p2:
            p2=d
#        print("dd",d)


distcalc(towns,0,None)

print("1:",p1)
print("2:",p2)
