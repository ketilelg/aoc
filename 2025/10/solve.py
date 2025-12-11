import sys
from collections import defaultdict
import re
from functools import cache
import itertools
from copy import deepcopy

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


    val=[0]*len(jtarget)

    # gjenstår: kjør fra lengst keyset og ned.. vi 

    def testp(jtarget,j,pos,np,v):
        print("testp",pos,"v",v,"np",np,"j",j)
        jbset=deepcopy(j)
        if pos>=len(jtarget):
            return
        # if pos>0: #noe har skjedd, fjern knapper vi ikke kan bruke fra jbset
        #     i=pos-1
        #     for b in j[i]:
        #         for jj,js in enumerate(jbset):
        #             if b in js:
        #                 jbset[jj].remove(b)
        longest=0 #lengste keyset
        for ji,jj in enumerate(jbset):
#            print(" ll",ji,jj)
            if len(jj)>longest:
                longest=ji
        print("pos",longest)
        pos=longest
#        maxp=1000000
        # for b in jbset[pos]:
        #     print("  fmp",b)
        #     for j in intb[b]:
        #         print("    ffmp",j,jtarget[j],v[j])
        #         if (jtarget[j]-v[j]) < maxp:
        #             maxp=jtarget[j]-v[j]
        maxp=jtarget[pos]-v[pos]
        print("maxp",maxp,pos,jbset,v)
#        for ps in perms(jtarget[pos]-v[pos],len(jbset[pos])):
        for ps in perms(maxp,len(jbset[pos])):
            npress=np
            over=False
            val=v.copy()
            print("ps",pos,ps,val,jbset[pos])
            for i,p in enumerate(ps): #[1,2] - first button 1, second 2.  
#                print(" vv",jbset[pos][i],val,pos,i,p)
                for b in intb[jbset[pos][i]]:
                    val[b]+=p
#                    print("  vvv",val,b,p)
                    if val[b]>jtarget[b]:
                        over=True
                npress+=p
            if over:
                continue
            print("val",pos,val,jtarget)
            if val==jtarget:
                print("hoihoival",pos,npress,val)
            # på tide med rekursjon:
            else:
                # remove used keybs
                for b in j[pos]:
                    jb=deepcopy(jbset)
                    for jj,js in enumerate(jbset):
                        if b in js:
                            jb[jj].remove(b)

                testp(jtarget,jb,pos,npress,val)
                # pp=0
                # while (pp<len(val)) and (val[pp]==jtarget[pp]):
                #     pp+=1
                # if pp==len(val):
                #     print("valhoi2",val)
                # elif pp<len(val):
                #     print("-rec",pp,val,jbset)
                #     testp(jtarget,jbset,pp,npress,val)
                # else:
                #     print("wtf??")
                #     exit()

    testp(jtarget,jbset,0,0,val)
#    while True:
#        for i,jj in enumerate(jtarget):



print("1:",p1)
print("2:",p2)
