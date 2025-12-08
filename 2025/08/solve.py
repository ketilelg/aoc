import sys
import math

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

jb=[]
for l in inp:
    jb.append((tuple(map(int,l.split(",")))))

dists=[]
for i in range(len(jb)):
    for j in range(i+1,len(jb)):
        dists.append((math.dist(jb[i],jb[j]),jb[i],jb[j]))

sets=[] #de forskjellige kretsene, liste av sets
dists.sort()

maxlen=0
conns=0
for i in dists: #mulige connections
    conns+=1
    used=False
    # finn om denne koplingen har et bein:
    for sn in range(len(sets)):
        s=sets[sn]
        if (i[1] in s) and (i[2] in s): #dette paret finnes i en krets, gir oss ikke noe nytt
            used=True
        elif (i[1] in s) or (i[2] in s): #et bein finnes i det minste
            for sn2 in range(sn+1,len(sets)): #kopler denne koplingen sammen to kretser?
                s2=sets[sn2]
                if (i[1] in s2) or (i[2] in s2):
                    s = s | s2 # kombiner
                    sets.pop(sn2) #fjern 
                    used=True
                    break                       
            s = s | {i[1],i[2]}
            sets[sn]=s
            if len(s)>maxlen:
                maxlen=len(s)
            used=True
            break
    if not used:
        sets.append({i[1],i[2]})


    if conns==1000:
        p1=math.prod(sorted([len(l) for l in sets])[-3:])
    #see if we have all connected..:
    if maxlen==len(jb):
        p2=i[1][0]*i[2][0]
        break

lens=[]


print("1:",p1)
print("2:",p2)
