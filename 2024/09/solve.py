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
#    print("ff",pos,map[pos],map[pos+1])
    for i in range(inp[pos]):
        emap.append(id)
    if pos < l-1:
        for i in range(inp[pos+1]):
            emap.append(".")
    id+=1
    pos+=2

space=inp[0] #første ledige plass
lastblock=len(emap)-1

# print("spl",space,lastblock)

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

# print("spl",space,lastblock)

# print("ee",emap)


p2map=[]
pos=0
l=len(inp)
id=0
while(pos<l):
#    print("ff",pos,map[pos],map[pos+1])
    for i in range(inp[pos]):
        p2map.append(id)
    if pos < l-1:
        for i in range(inp[pos+1]):
            p2map.append(".")
    id+=1
    pos+=2

print("pp",p2map)

space=inp[0]
spacelen=inp[1]
lastblock=len(inp)-1
lastmpos=len(p2map)-1
id=0
lastid=int(lastblock/2)
while(lastid>0):
    print("sdf",lastblock,space,lastid,lastmpos)
    print("em",p2map,inp)

#    finn evt ledig plass:
    moved=False
    spos=1
    while spos < lastblock and inp[spos] < inp[lastblock]:
        print("movetest",spos,inp[spos],inp[lastblock],lastid,spos,lastblock)
        spos+=2
    print("spos",spos)
    smpos=0
    for j in range(spos):
        smpos+=inp[j]
    print("spos",spos,smpos)
    if spos<lastblock:
        #vi kan flytte
        for i in range(inp[lastblock]):
            p2map[smpos+i],p2map[lastmpos-i]=p2map[lastmpos-i],p2map[smpos+i]

        print("moved:",p2map)
        inp[spos-1]+=inp[lastblock]
        inp[spos]-=inp[lastblock]
        
#    if map[lastblock]<=spacelen:
#        for i in range(map[lastblock]):
#            p2map.[space+i]=lastid
    lastmpos-=inp[lastblock]+inp[lastblock-1]
    lastblock-=2
    lastid-=1

    id+=1
    pos+=2

    

pos=0
while emap[pos] !=".":
    p1+=emap[pos]*pos
    pos+=1

pos=0
print("p2map",p2map)
for i in range(len(p2map)):
    if p2map[i]!=".":
        p2+=i*p2map[i]


print("1:",p1)
print("2:",p2)
