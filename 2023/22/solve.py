import math
import copy
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    stones = [list(map(int,s.replace("~",",").split(","))) for s in f.read().strip().split("\n")]



#dette er for testing:
xlist=list(b[x] for x in (0,3) for b in stones)
ylist=list(b[x] for x in (1,4) for b in stones)
zlist=list(b[x] for x in (2,5) for b in stones)

print("x",max(xlist),min(xlist))
print("y",max(ylist),min(ylist))
print("z",max(zlist),min(zlist))




# alle bricks er sortert med nedre venstre hjørne først.

#sorter steiner etter høyde, lavest først:
def lowz(elem):
    return(elem[2])

stones.sort(key=lowz)

newstones=[]

# print("oldstones",stones)

#newstons[n][6] er antall supports..:

def faller(s):
    print("falling..",s[:6])
    #kan s flytte ned?
    nsupp=0 #how many support this?
    while((s[2]>1) and (nsupp==0)):
        #se om det er noe nedenfor vi kan krasje i ved å gå en ned
        #
        for t in reversed(newstones):
            if (not((s[0]>t[3]) or (s[3]<t[0]) or (s[1]>t[4]) or (s[4]<t[1])) and (s[2]-1 == t[5])):
                nsupp+=1
                t[8]+=1
                t[6].append(s)
#                break
        if(nsupp==0):
            s[2]-=1
            s[5]-=1
    s[9]=nsupp
    s[10]=nsupp
    newstones.append(s)



for s in stones:
    print("falling..",s[:6])
    #kan s flytte ned?
    nsupp=0 #how many support this?
    s.append([])
    s.append([])
    s.append(0)
    s.append(0)
    s.append(0)
    while((s[2]>1) and (nsupp==0)):
        #se om det er noe nedenfor vi kan krasje i ved å gå en ned
        #
        for t in reversed(newstones):
            if (not((s[0]>t[3]) or (s[3]<t[0]) or (s[1]>t[4]) or (s[4]<t[1])) and (s[2]-1 == t[5])):
                nsupp+=1
                t[8]+=1
                t[6].append(s)
#                break
        if(nsupp==0):
            s[2]-=1
            s[5]-=1
    s[9]=nsupp
    s[10]=nsupp
    newstones.append(s)


print("newstones",newstones)





for s in newstones:
    print("stone",s[:6],len(s[6]),len(s[7]),s[8],s[9],s[10])
    if(s[8]==0): #støtter ingen
       s1+=1
    else:
        ok=True
        for tt in s[6]:
            print("  tt",tt[:5],tt[9])
            ok=ok and (tt[9] >1)
        if(ok):
            s1+=1


print("1:", s1)
    
print("2:", s2)

# 105157 too high
