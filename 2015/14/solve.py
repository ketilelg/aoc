import sys
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


limit=2503
#limit=1000

birdp={}
birdd={}
dirsc={}
for b in inp:
    ll=b.split(" ")
    name=ll[0]
    birdp[name]=0
    dirsc[name]=0
    speed=int(ll[3])
    flight=int(ll[6])
    rest=int(ll[13])
    birdd[name]=(speed,flight,rest)
    dist=((limit//(flight+rest))*speed*flight)+(speed*(min(limit%(flight+rest),flight)))
    if dist>p1:
        p1=dist

for i in range(1,limit+1):
    for b in birdp:
        speed,flight,rest=birdd[b]
        birdp[b]=((i//(flight+rest))*speed*flight)+(speed*(min(i%(flight+rest),flight)))

    maxd=max(birdp.values())
    p1=maxd
    for b in birdp:
        if birdp[b]==maxd:
            dirsc[b]+=1

#print("sdf",dirsc)
print("1:",p1) 
print("2:",max(dirsc.values()))
