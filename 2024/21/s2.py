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



def mrange(f,t):
    if t>=f:
        return range(f,t+1)
    else:
        return reversed(range(t,f+1))

def npfromto(k,sx,sy,tx,ty):
    #returns best movestring from sx,sy to tx,ty
    if k[sy][sx]=="*":
        return["*"]
    if tx>sx:
        dxm=">"
    else:
        dxm="<"
    if ty>sy:
        dym="^"
    else:
        dym="v"

    if sx==tx: #up/down:
        return([dym*abs(ty-sy)])
    elif sy==ty: #r/l
        return([dxm*abs(tx-sx)])
    else: #skrå, begge ulike
        if k[sy][tx]=="*":  # * i samme rad, kun h før v
            return([dym*abs(ty-sy)+dxm*abs(tx-sx)])
        elif k[ty][sx]=="*":  # * i samme kolonne, kun v før h
            return([dxm*abs(tx-sx)+dym*abs(ty-sy)])
        else: # ingen * i veien, begge veier kan være aktuelle
            if dxm=="<":
                return([dxm*abs(tx-sx)+dym*abs(ty-sy)])
            else:
                return([dym*abs(ty-sy)+dxm*abs(tx-sx)])


def numfromto(k,n,f,t):
    return(npfromto(k,n[f][0],n[f][1],n[t][0],n[t][1]))           

def moves(k,n,keys):
    # return list of possible ways to achieve keys.. keys is list of keys
    s="A"
    t=keys.pop(0)
#    print("sdf",keys,s,t)
    sols={""}
    while True:
        r=numfromto(k,n,s,t)
        ii=sols.copy()
        for s in ii:
            for rr in r:
#                print(" frr",rr,sols)
                nnn=s+rr+"A"
#                print("  fs",nnn,s,rr,sols)
                sols.add(nnn)
            sols.remove(s)

        s=t
        if not keys:
            return sols
        t=keys.pop(0)


for li in inp:
#    print("l",li)
    l=list(li)

    ss=[]
    ss.append({li:1})

#    print("\n\nss",ss)
    nsol=[]
    for sol in ss:
        # vi har en "løsning" sol, som er delt opp i delløsninger:
        for m in sol:
#            print("mm",m,sol[m])
            mult=sol[m]
            res1=moves(numk,nump,list(m))
#            print("rr",res1)
            for r in res1:
                rdi=defaultdict(int)
                pmoves=re.findall(r"([<>v^]*A)",r)
#                print(" rrr",r,pmoves)
                for pm in pmoves:
                    rdi[pm]+=mult
#                print(" rre",rdi)
                nsol.append(rdi)

    minl=1000000000000000000
    for n in range(len(nsol)):
#        print("nsol",n,nsol[n],end="")
        l=0
        for p in nsol[n]:
            l+=len(p)*nsol[n][p]
#        print("l:",l)
        if l<minl:
            minl=l




    ss=nsol
#    print("\n\n-----ss2",len(ss))
    nsol=[]
    for sol in ss:
#        print(" sol22",sol)
        # vi har en "løsning" sol, som er delt opp i delløsninger:
        solres=[defaultdict(int)] #list of possible solutions, as dicts
        smult=1 #number of parallell solutions as of now
        for m in sol:
#            print("  mm",m,sol[m])
            mult=sol[m]
            res1=moves(arrk,arrp,list(m))
            if len(res1)>1:
                #øk solres-tabellen så mange ganger:
                resl=len(solres)
                for n in range(resl*(len(res1)-1)):
                    solres.append(solres[n%resl].copy())
 #           print("  rr2",len(res1),res1)
            ind=0
            for r in res1:
                pmoves=re.findall(r"([<>v^]*A)",r)
 #               print("   rrr2",r,pmoves,ind,smult)
                for pm in pmoves:
#                    print("pppppp",pm)
                    for ii in range(smult):
#                        print("iiiii",ind,ii,smult,solres)
                        solres[ind+ii][pm]+=mult
                ind+=smult
            smult*=len(res1)
        for sr in solres:
            ll=0
            for mm in sr:
                ll+=len(mm)*sr[mm]
#            print("  solres",ll,sr)
            nsol.append(sr)

    minl=1000000000000000000

    for n in range(len(nsol)):
  #      print("nsol2",n,nsol[n],end="")
        l=0
        for p in nsol[n]:
            l+=len(p)*nsol[n][p]
  #      print("l:",l)
        if l<minl:
            minl=l
#    print("sdfsdf1",len(nsol))

    count=0
    while count<25:
        count+=1

        ss=nsol
#        print("\n\n-----ss3",minl,len(ss))
        nsol=[]
        for sol in ss:
#            print(" sol33",sol)
            l=0
            for p in sol:
                l+=len(p)*sol[p]
            if l>minl:
                continue
            # vi har en "løsning" sol, som er delt opp i delløsninger:
            solres=[defaultdict(int)] #list of possible solutions, as dicts
            smult=1 #number of parallel solutions as of now
            for m in sol:
    #            print("  mm",m,sol[m])
                mult=sol[m]
                res1=moves(arrk,arrp,list(m))
                if len(res1)>1:
                    #øk solres-tabellen så mange ganger:
                    resl=len(solres)
                    for n in range(resl*(len(res1)-1)):
                        solres.append(solres[n%resl].copy())
    #            print("  rr2",len(res1),res1)
                ind=0
                for r in res1:
                    pmoves=re.findall(r"([<>v^]*A)",r)
    #                print("   rrr2",r,pmoves,ind,smult)
                    for pm in pmoves:
    #                    print("pppppp",pm)
                        for ii in range(smult):
    #                        print("iiiii",ind,ii,smult,solres)
                            solres[ind+ii][pm]+=mult
                    ind+=smult
                smult*=len(res1)
            for sr in solres:
                ll=0
                for mm in sr:
                    ll+=len(mm)*sr[mm]
    #            print("  solres",ll,sr)
                nsol.append(sr)

        minl=10000000000000000000

        for n in range(len(nsol)):
#            print("nsol",count,n,nsol[n],end="")
            l=0
            for p in nsol[n]:
                l+=len(p)*nsol[n][p]
#            print("l:",l)
            if l<minl:
                minl=l
        if count==1:
            print("P1SUM",li,minl,len(nsol))
            p1+=minl*int(li[:-1])
        if count==24: #should be 24 for reals
            print("P2SUM",li,minl,len(nsol))
            p2+=minl*int(li[:-1])
#        print("count",count,len(nsol))


print("1:",p1,p1==152942) #152942 
print("2:",p2)

