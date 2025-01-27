import sys
import itertools

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    packs = set(map(int,f.read().strip().split("\n")))

p1=p2=0
    
print("ss",sum(packs),sum(packs)/3,3**len(packs))

pack3=int(sum(packs)/3)

sols=set()

#for i in range(3,len(packs)):

def findfirst(packs,sols,target,limit):
    i=2
    done=False
    while i<limit:
        pp=list(itertools.combinations(packs,i))
        for p in pp:
            if sum(p)==target:
                sols.add(p)
    #            print("pp",i,p)
                done=True
        i+=1


def findp(restp,pset,sum,target):
    if sum<target:
        for p in restp:
            if p+sum==target:
#                print("sum!",pset)
                return True
#                findp(restp-{p},set(),0,pre+" ")
            elif p+sum<target:
                return findp(restp-{p},pset | {p},sum+p,target)
    return False

p1=10000000000000000000
pack3=int(sum(packs)/3)
sols=set()
findfirst(packs,sols,pack3,7)
for s in sols:
    if findp(set(packs) - set(s),set(), 0, pack3):
#        print("hoi!",s)   
        qe=1
        for f in s:
            qe*=f
        if qe<p1:
            p1=qe


# findp(set(packs),set(),0,"")

print("1:",p1)

p2=10000000000000000000
pack4=int(sum(packs)/4)
sols=set()
findfirst(packs,sols,pack4,7)
for s in sols:
    qe=1
    for f in s:
        qe*=f
    if qe<p2:
#    print("sss",s)
        sols2=set()
        findfirst(packs-set(s),sols2,pack4,8)
        for ss in sols2:
            if findp(set(packs) - set(ss) -sols2,set(), 0, pack4):
    #            print("hoi!",ss)   
                p2=qe
#                print("p2",p2)
                break

print("2:",p2)
