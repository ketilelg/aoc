import sys
from collections import defaultdict
import re
from functools import cache
import itertools


with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

for l in inp:
#    print("l",l.split(" "))
    ls=l.split(" ")
    lights=ls[0]
    buttons=ls[1:-1]
    jolts=ls[-1]
    best=100
    found=False
    print("sss",lights,buttons,jolts,len(lights))
    for i in range(1,len(buttons)):
        kc=itertools.combinations(buttons,i)
        for c in kc:
            res=""
#            print("  ii",i,list(c),"".join(c))
            for j in range(len(lights)-2):
                if "".join(c).count(str(j))%2==1:
                    res+="#"
                else:
                    res+="."
#            print(" rr",res,lights[1:-1])
            if res  == lights[1:-1]:
#                print("jepp")
                found=True
                npress=len(c)
                if npress<best:
                    best=npress
                break
        if found:
            break
    p1+=best

    found=False     
    jtarget=list(map(int,jolts[1:-1].split(",")))

    intb=[]
    for b in buttons:
        intb.append(tuple(map(int,b[1:-1].split(","))))
    print("ii",intb)
    for n in itertools.count(max(jtarget)):
#        ll=itertools.combinations_with_replacement(buttons,n)
        print("trying",n)

#         for b in ll:
#             jj=[0]*(len(jtarget))
#             ss="".join(b)
# #            print("bb",len(ss))
#             for p in range((len(jj))):
#                 jj[p]=ss.count(str(p))
#             if jj==jtarget:
#                 print("ff",n)
#                 found=True
#                 p2+=n
#                 break              
        if n>10:
            found=True
        if found:
            break


print("1:",p1)
print("2:",p2)
