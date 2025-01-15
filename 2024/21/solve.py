import sys
import re
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")



p1=p2=0

numk=[["*","0","A"],
      ["1","2","3"],
      ["4","5","6"],
      ["7","8","9"]]
nump={"A":(2,0),
      "0":(1,0),
      "1":(0,1),
      "2":(1,1),
      "3":(2,1),
      "4":(0,2),
      "5":(1,2),
      "6":(2,2),
      "7":(0,3),
      "8":(1,3),
      "9":(2,3)}


arrk=[["<","v",">"],
      ["*","^","A"]]

arrp={"A":(2,1),
      "^":(1,1),
      "<":(0,0),
      "v":(1,0),
      ">":(2,0)}


def numfromto(k,n,f,t):
    #returns best movestring from f to t
    sx=n[f][0]
    sy=n[f][1]
    tx=n[t][0]
    ty=n[t][1]
    if tx>sx:
        dxm=">"
    else:
        dxm="<"
    if ty>sy:
        dym="^"
    else:
        dym="v"

    if sx==tx: #up/down:
        return(dym*abs(ty-sy))
    elif sy==ty: #r/l
        return(dxm*abs(tx-sx))
    else: #skrå, begge ulike
        if k[sy][tx]=="*":  # * i samme rad, kun h før v
            return(dym*abs(ty-sy)+dxm*abs(tx-sx))
        elif k[ty][sx]=="*":  # * i samme kolonne, kun v før h
            return(dxm*abs(tx-sx)+dym*abs(ty-sy))
        else: # ingen * i veien, begge veier kan være aktuelle, men dette er best:
            if dxm=="<":
                return(dxm*abs(tx-sx)+dym*abs(ty-sy))
            else:
                return(dym*abs(ty-sy)+dxm*abs(tx-sx))



def moves(k,n,keys):
    # return list of possible ways to achieve keys.. keys is list of keys
    s="A"
    t=keys.pop(0)
    sol=[]
    while True:
        sol.append(numfromto(k,n,s,t)+"A")
        if not keys:
            return sol
        s=t
        t=keys.pop(0)


for li in inp:
#    print("l",li)

    res1=moves(numk,nump,list(li))

#    print("res1",res1,li)
    sol=defaultdict(int)
    for pm in res1:
        sol[pm]+=1

    count=0
    while count<26:
        count+=1
        nsol=defaultdict(int)
        for m in sol:
            mult=sol[m]
            res1=moves(arrk,arrp,list(m))
            for r in res1:
                nsol[r]+=mult
        ll=0
        sol=nsol
        for m in sol:
            ll+=len(m)*sol[m]
        if count==2:
#            print("P1SUM",li,ll,len(nsol))
            p1+=ll*int(li[:-1])
        if count==25: #should be 24 for reals
#            print("P2SUM",li,ll,len(nsol))
            p2+=ll*int(li[:-1])
#        print("count",count,len(nsol))


print("1:",p1,p1==152942) #152942 
print("2:",p2)

