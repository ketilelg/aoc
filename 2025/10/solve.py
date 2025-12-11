import sys
from collections import defaultdict
import re
from functools import cache
import itertools


with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

def perms(sum, k): #stjælt fra nettet. genererer liste av alle permutasjoner
    if k < 1:
        return []
    if k == 1:
        return [(sum,)]
    if k == 2:
        return [(i,sum-i) for i in range(0, sum-k+3)]
    
    return [tup[:-1] + ab for tup in perms(sum, k-1) for ab in perms(tup[-1], 2)]

#print("pp",perms(4,3))
#exit()

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
    ujtarget=list(map(int,jolts[1:-1].split(",")))

    uintb=[]
    for b in buttons:
        uintb.append(list(map(int,b[1:-1].split(","))))
    ujbset=[]
    for j in range(len(ujtarget)):
        bs=[]
        for bi,b in enumerate(uintb):
            if j in b:
                bs.append(bi)
        ujbset.append(bs)
    print("ii",uintb,"\n ",ujtarget,"\n ",ujbset)

    sorta=[]
    smap={}
    for i,j in enumerate(ujbset):
        sorta.append([len(j),i,ujtarget[i],j])
    for ss in sorta:
        print("  iii",ss)
    sorta.sort(reverse=True)
    for i,ss in enumerate(sorta):
        smap[sorta[i][1]]=i
        print("  iis",ss)
    intb=[]
    print("  sm",smap)
    for i,b in enumerate(uintb):
        print(" b",i,b)
        nb=[]
        for bb in b:
            nb.append(smap[bb])
        intb.append(nb)
    jtarget=[]
    jbset=[]
    for ss in sorta:
        jtarget.append(ss[2])
        jbset.append(ss[3])

    val=[0]*len(jtarget)

    def testp(jtarget,jbset,pos,np,v):
        # må ha med trykk brukt, sånn at vi ikke prøver å bruke fler
        # i neste runde. (dvs: knapper som ikke kan testes nå, fordi ferdigtrykket)
        print("testp",pos,v,np,jbset[pos])
        if pos>=len(jtarget):
            return
        for i in range(pos):
            for b in jbset[i]:
                if b in jbset[pos]:
                    jbset[pos].remove(b)
        for ps in perms(jtarget[pos]-v[pos],len(jbset[pos])):
            npress=np
            over=False
            val=v.copy()
#            print("ps",pos,ps,val,jbset[pos])
            for i,p in enumerate(ps): #[1,2] - first button 1, second 2.  
 #               print(" vv",jbset[pos][i],val,pos,i,p)
                for b in intb[jbset[pos][i]]:
                    val[b]+=p
 #                   print("  vvv",val,b,p)
                    if val[b]>jtarget[b]:
                        over=True
                npress+=p
            print("val",pos,val)
            if val==jtarget:
                print("hoihoi",pos,npress,val)
            # på tide med rekursjon:
            elif not over:
                testp(jtarget,jbset,pos+1,npress,val)

    testp(jtarget,jbset,0,0,val)
#    while True:
#        for i,jj in enumerate(jtarget):



print("1:",p1)
print("2:",p2)
