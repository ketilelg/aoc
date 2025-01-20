import sys
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=00
p2=0

persons={}
for i in inp:
    ll=i.split(" ")
#    print("ll",ll[0],ll[2],ll[3],ll[10][:-1])
    gain=int(ll[3])
    if ll[2]=="lose":
        gain=-gain
    p=ll[0]
    n=ll[10][:-1]
    if not p in persons:
        persons[p]={}
    persons[p][n]=gain

pnames=set(persons.keys())

# print("pp",persons)
# print("pl",pnames)

def testp(inp,pset,plist):
    global p1
#    print("\ntestp",pset,plist)
    if pset:
        for p in pset:
            pp=plist.copy()
            pp.append(p)
            ps=pset.copy()
            ps.remove(p)
            testp(p,ps,pp)
    else:
        sc=0
        for i in range(len(plist)):
            if i==0:
                sc=persons[plist[i]][plist[i+1]]
                sc+=persons[plist[i]][plist[-1]]
            else:
                sc+=persons[plist[i]][plist[(i+1)%len(plist)]]
                sc+=persons[plist[i]][plist[i-1]]
#        print("  plist",plist,sc)
        if sc>p1:
            p1=sc

first=pnames.pop()

testp(first,pnames,[first])
print("1:",p1)

persons["Me"]={}
for p in persons:
    persons["Me"][p]=0
    persons[p]["Me"]=0
pnames.add("Me")

p1=0
testp(first,pnames,[first])

print("2:",p1)
