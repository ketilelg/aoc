import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    map = f.read().strip().split("\n")


w=len(map[0])
h=len(map)

hempty=[]
for ln,l in enumerate(map):
#    print(l)
    empty=1
    for c in l:
        empty = empty and (c==".")
    if(empty):
        hempty.append(ln)
vempty=[]
gal=[]
for cn,c in enumerate(map[0]):
    empty=1
    for l in range(h):
        empty=empty and (map[l][cn] == ".")
        if(map[l][cn]=="#"):
            gal.append((cn,l))
    if(empty):
        vempty.append(cn)
            
# print("hempty",hempty)        
# print("vempty",vempty)        
# print("gal",gal)


dists=0
dist2=0
for g in gal:
#    print("\ng",g)
    for g2 in gal:
#        print("g2",g2)
        #finn vertikale exps:
        vs=0
        for v in range(min(g[0],g2[0]),max(g[0],g2[0])):
            if(v in vempty):
                vs+=1
#        print("vs",vs)
        #finn h exps:
        hs=0
        for h in range(min(g[1],g2[1]),max(g[1],g2[1])):
            if(h in hempty):
                hs+=1


        dists+=abs(g[0]-g2[0])+abs(g[1]-g2[1])+((vs+hs))
        dist2+=abs(g[0]-g2[0])+abs(g[1]-g2[1])+(999999*(vs+hs))
#        print("vs",vs,hs,dists,dist2)

print("1:", int(dists/2))


print("2:", int(dist2/2))

