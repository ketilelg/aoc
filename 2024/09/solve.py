import sys
import copy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    map = list(f.read().strip())

p1=p2=0

emap=[]
pos=0
l=len(map)
id=0
while(pos<l):
#    print("ff",pos,map[pos],map[pos+1])
    for i in range(int(map[pos])):
        emap.append(id)
    if pos < l-1:
        for i in range(int(map[pos+1])):
            emap.append(".")
    id+=1
    pos+=2

space=int(map[0]) #første ledige plass
lastblock=len(emap)-1

print("spl",space,lastblock)

while lastblock>space:
    emap[space],emap[lastblock]=emap[lastblock],emap[space]
#    print("w",emap,space,lastblock,end="")
    space+=1
    lastblock-=1
    while emap[space]!="." and space<lastblock:
        space+=1
    while emap[lastblock]=="." and lastblock>space:
        lastblock-=1
#    print(" - ",space,lastblock)

print("spl",space,lastblock)

print("ee",emap)

p2map=[]
space=int(map[0]) #første ledige plass
lastblock=len(map)-1
lastid=int(lastblock/2)
while(lastblock > space):
    print("sdf",lastblock,space,lastid)
    

pos=0
while emap[pos] !=".":
    p1+=emap[pos]*pos
    pos+=1

print("1:",p1)
print("2:",p2)
