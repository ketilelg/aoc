import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    maps =  [[list(l) for l in s.split("\n")] for s in f.read().strip().split("\n\n")]

def printmap(m):
    for l in m:
        print(l)


nv=0
nh=0

def findm(m):
    #returns (besth,bestv,hset,vset):
    #besth - best possible h mirror (if any)
    #bestv - best possible v mirror (if any)
    #hset - set of h mirrors
    #vset - set of v mirrors
    #find h mirrors:
    w=len(m[0])
    mhpos=0
    mhbest=0
    hlist=set()
    while ((mhpos<w-1)):
        #test if mhpos is a mirror:
        mhpos+=1
        ism=True

        #d is how far we can go from mhpos
        for d in range(min(mhpos,(w-mhpos))):
            for l in m:
                #is this line mirrored at mhpos?
                cl=l[mhpos-d-1]
                cr=l[mhpos+d]
                ism=(cl == cr ) and ism

        if(ism):

            mhbest=mhpos
            hlist.add(mhpos)

    h=len(m)
    mvpos=0
    mvbest=0
    vlist=set()
    while ((mvpos<h-1)):
        #test if mvpos is a mirror:
        mvpos+=1
        ism=True

        #d is how far we can go from mvpos
        for d in range(min(mvpos,(h-mvpos))):

            if(m[mvpos-d-1] != m[mvpos+d]):
                ism=False
            else:
                ism=ism and True
                    
        if(ism):
            mvbest=mvpos
            vlist.add(mvpos)

    return((mhbest,mvbest,hlist,vlist))

for m in maps:

    mh,mv,mhl,mvl=findm(m)
    s1+=(100*mv)+mh

    nhl=set() #set of possible mirrors
    nvl=set()

    for x in range(len(m[0])):
        for y in range(len(m)):
            m[y][x]="." if m[y][x]=="#" else "#"
            mh2,mv2,mhl2,mvl2=findm(m)

            nhl.update(mhl2)
            nvl.update(mvl2)
            #revert 
            m[y][x]="." if m[y][x]=="#" else "#"

    nhset=nhl.difference(mhl)
    nvset=nvl.difference(mvl)

    if(len(nhset)>0):
       s2+=nhset.pop()
    if(len(nvset)>0):
       s2+=nvset.pop()*100
            
print("1:", int(s1))

print("2:", int(s2))
