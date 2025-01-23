import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


ingr={}
ingp={}


for b in inp:
    name,rest=b.split(":")
    print("rr",re.findall(r"\-?\d+",rest))
    ingr[name]=list(map(int,re.findall(r"\-?\d+",rest)))
    ingp[name]=0

def cscore(): #score without calories
    r=1
    for j in range(len(ingr[list(ingr.keys())[0]])-1): #-1 to avoid calories
        rr=0
        for i in ingp:
            rr+=ingr[i][j]*ingp[i]
        if rr<0: 
            rr=0
#        print("fj",rr,r)
        r*=rr
    cal=0
    for i in ingp:
        cal+=ingr[i][4]*ingp[i]

    return r,cal

print("i",ingr)
#ingp["Butterscotch"]=44
#ingp["Cinnamon"]=56
#print("scsc",cscore())

for a in range(1,98):
    for b in range(1,99-a):
        for c in range(1,100-(a+b)):
#            print("abcd",a,b,c,100-(a+b+c))
            ingp["Frosting"]=a
            ingp["Candy"]=b
            ingp["Butterscotch"]=c
            ingp["Sugar"]=100-(a+b+c)
            r,c=cscore()
            if r>p1:
                p1=r
            if c==500 and r>p2:
                p2=r
#            for d in range(1,98-(a+b+c)):
#                print("abcd",a,b,c,d a+b+c+d)

print("1:",p1) 
print("2:",p2)
