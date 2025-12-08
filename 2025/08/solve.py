import sys
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
    jb.append((tuple(map(int,l.split(",")))))


dists=[]
for i in range(len(jb)):
    for j in range(i+1,len(jb)):
        if i!=j:
            d=dist(jb[i],jb[j])
            dists.append((d,jb[i],jb[j]))

sets=[] #de forskjellige kretsene, liste av sets
dists.sort()

conns=0
for i in dists: #mulige connections
    conns+=1
    used=False
    # finn om denne koplingen er på plass allerede:
    for sn in range(len(sets)):
        s=sets[sn]
        if (i[1] in s) and (i[2] in s): #dette paret finnes i en krets, gir oss ikke noe nytt
            used=True
            break
        elif (i[1] in s) or (i[2] in s):
            for sn2 in range(sn+1,len(sets)):
                s2=sets[sn2]
                if (i[1] in s2) or (i[2] in s2):
                    s = s | s2 # kombiner
                    sets[sn2]=set() #fjern 
                    used=True
                    break                       
            s = s | {i[1],i[2]}
            sets[sn]=s
            used=True
            break
    if not used:
        sets.append({i[1],i[2]})

    lens=[]
    for s in sets:
        lens.append(len(s))

    if conns==1000:
        lens.sort()
        p1=math.prod(lens[-3:])

    #see if we have all connected..:
    if max(lens)==len(jb):
        p2=i[1][0]*i[2][0]
        break

lens=[]


print("1:",p1)
print("2:",p2)
