import sys
from collections import defaultdict
import re
from functools import cache
import math

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

def sq(v):
    return v*v

def dist(p1,p2):
    return math.sqrt(sq(p1[0]-p2[0])+sq(p1[1]-p2[1])+sq(p1[2]-p2[2]))

jb=[]
for l in inp:
#    print("l",l)
    jb.append((tuple(map(int,l.split(",")))))

print("j",jb)

mindist=100000000000000
min1= -1
min2= -1
dists=[]
for i in range(len(jb)):
    for j in range(i+1,len(jb)):
        if i!=j:
            d=dist(jb[i],jb[j])
            dists.append((d,jb[i],jb[j]))
            if d<mindist:
#                print("min",d)
                min1=i
                min2=j    
                mindist=d

# print("min",min1,min2,jb[min1],jb[min2])
setls=[] #lengder av sett. trenger kanskje ikke denne.
sets=[] #de forskjellige kretsene, liste av sets
nset=set()
tset=set()
dists.sort()
conns=0
nset.add(dists[0][1])
nset.add(dists[0][2])
for i in dists:
    print("\n\nii",i)
    used=False
    for sn in range(len(sets)):
        s=sets[sn]
        print("4s",s,i)
        if (i[1] in s) or (i[2] in s):
            lls=len(s)
            s = s | {i[1],i[2]}
            if lls<len(s):
                conns+=1
            sets[sn]=s
            print("in",s)
            used=True
            break
    if not used:
        sets.append({i[1],i[2]})
        conns+=1

    # if ((i[1] not in tset) and (i[2] not in tset)):
    #     if ((i[1] in nset) or (i[2] in nset)):
    #         nset.add(i[1])
    #         nset.add(i[2])
    #         conns+=1
    #         print("conn",conns,nset)
    #     else:
    #         conns+=1
    #         print("unloop",conns,len(nset),nset)
    #         setls.append(len(nset))
    #         tset= tset|nset
    #         nset={i[1],i[2]}
    if conns>1000:
        break            

lens=[]

# slå sammen mangdene..
newsets=set()
for s in sets:
    ns=s
    added=False
    for x in newsets:
        if (ns & x): #de overlapper
            ns = ns | x
            added=True
    # gurk. noe mangler her. 
for s in sets:
    print("sss",s)
    lens.append(len(s))

lens.sort()
p1=math.prod(lens[-3:])
print("ss",lens,lens[-3:])        

print("1:",p1)
print("2:",p2)
