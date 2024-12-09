import sys
import copy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,list(f.read().strip())))

p1=p2=0

emap=[]
pos=0
l=len(inp)
id=0
while(pos<l):
    for i in range(inp[pos]):
        emap.append(id)
    if pos < l-1:
        for i in range(inp[pos+1]):
            emap.append(".")
    id+=1
    pos+=2

p2map=emap.copy()
space=inp[0] #første ledige plass
lastblock=len(emap)-1

while lastblock>space:
    emap[space],emap[lastblock]=emap[lastblock],emap[space]
    space+=1
    lastblock-=1
    while emap[space]!="." and space<lastblock:
        space+=1
    while emap[lastblock]=="." and lastblock>space:
        lastblock-=1

p2inp=inp.copy()

space=inp[0]
spacelen=inp[1]
lastblock=len(inp)-1
lastmpos=len(p2map)-1
id=0
lastid=int(lastblock/2)
while(lastid>0):
    print("li",lastid)
    moved=False
    spos=1
    while spos < lastblock and inp[spos] < p2inp[lastblock]:
        spos+=2
    smpos=0
    for j in range(spos):
        smpos+=inp[j]
    if spos<lastblock:
        for i in range(p2inp[lastblock]):
            p2map[smpos+i],p2map[lastmpos-i]=p2map[lastmpos-i],p2map[smpos+i]
        inp[spos-1]+=inp[lastblock]
        inp[spos]-=inp[lastblock]
        inp[lastblock-1]+=inp[lastblock]
        inp[lastblock]=0
    lastmpos-=p2inp[lastblock]+p2inp[lastblock-1]
    lastblock-=2
    lastid-=1

    id+=1
    pos+=2

pos=0
while emap[pos] !=".":
    p1+=emap[pos]*pos
    pos+=1

pos=0
for i in range(len(p2map)):
    if p2map[i]!=".":
        p2+=i*p2map[i]

print("1:",p1)
print("2:",p2)
