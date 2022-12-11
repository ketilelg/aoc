#!/usr/bin/python3
import re

mitems=[]
mops=[]
mtest=[]
mtru=[]
mfal=[]
minsp=[0,0,0,0,0,0,0,0,0,0]
f=open('input')
for m in f.read().split("\n\n"):
    for l in m.split("\n"):
        if l.find("Monkey")==0:
            mn=l.split()[1].split(":")[0]
        elif l.find("Starting items") > 0:
            items=l.split(":")[1].split(",")
        elif l.find("Operation") > 0:
            op=l.split("= ")[1]
        elif l.find("Test") > 0:
            testv=l.split()[3]
        elif l.find("true") > 0:
            tto=l.split()[5]
        elif l.find("false") > 0:
            fto=l.split()[5]
    mitems.append(items)
    mops.append(op)
    mtest.append(int(testv))
    mtru.append(int(tto))
    mfal.append(int(fto))

mn=int(mn)
    
for round in range(20):
    for monkey in range(mn+1):
        for i in mitems[monkey]:
            minsp[monkey]+=1
            old=int(i)
            old=int(eval(mops[monkey])/3)
            if old%int(mtest[monkey]) == 0:
                mitems[mtru[monkey]].append(old)
            else:
                mitems[mfal[monkey]].append(old)
        mitems[monkey]=[]

minsp.sort(reverse=True)
print("p1",minsp[0]*minsp[1])
