import sys
from functools import cache
from copy import deepcopy
from pulp import *
import itertools

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

for l in inp:
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
            for j in range(len(lights)-2):
                if "".join(c).count(str(j))%2==1:
                    res+="#"
                else:
                    res+="."
            if res  == lights[1:-1]:
                found=True
                npress=len(c)
                if npress<best:
                    best=npress
                break
        if found:
            break
    p1+=best


#    found=False     
    jtarget=list(map(int,jolts[1:-1].split(",")))

    intb=[]
    for b in buttons:
        intb.append(list(map(int,b[1:-1].split(","))))
    jbset=[]
    for j in range(len(jtarget)):
        bs=[]
        for bi,b in enumerate(intb):
            if j in b:
                bs.append(bi)
        jbset.append(bs)
    print("ii",intb,"\n ",jtarget,"\n ",jbset,"\n\n")

    kk=list(map(str,range(len(intb))))
    js=list(map(str,range(len(jtarget))))
    kcost=[1]*len(intb)
    print("kk",kk)
    print("js",js)

    prob=LpProblem("jolts",LpMinimize)


    jvars= LpVariable.dicts("butts",indices=kk,lowBound=0,cat="Integer")

    print("jj",[jvars[i] for i in kk])
    prob+=lpSum([jvars[i] for i in kk])


    for i,j in enumerate(jtarget):
        jv=LpVariable(f"jolt_{i}",lowBound=j,upBound=j,cat="Integer")
        prob+=(lpSum([jvars[str(k)] for k in jbset[i]]) == j,f"con{i}",)

    print("prob:",prob,"\n\nkeyvars: ",jvars)
    prob.solve()
#    print("status",LpStatus[prob.status])
    for v in prob.variables():
#        print("vv",v.name,v.varValue)
        p2+=int(v.varValue)
print("1:",p1)
print("2:",p2)
