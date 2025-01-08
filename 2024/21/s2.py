import sys

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
    #returns movestring(s) from sx,sy to tx,ty
#    print("nf",sx,sy,tx,ty)
    if k[sy][sx]=="*":
        return["*"]
    if sx==tx: #up/down:
#        print(" UD")
        if sy<ty:
            return(["^"*abs(ty-sy)])
        else:
            return(["v"*abs(sy-ty)])
    elif sy==ty: #r/l
#        print(" LR")
        if sx<tx: #r
            return([">"*abs(tx-sx)])
        else:
            return(["<"*abs(sx-tx)])
    else: #skrå, begge ulike
        dx=int((tx-sx)/abs(tx-sx))
        dy=int((ty-sy)/abs(ty-sy))
        if dx==1:
            dxm=">"
        else:
            dxm="<"
        if dy==1:
            dym="^"
        else:
            dym="v"

#        print(" ss",sx,sy,tx,ty,dx,dy)
        lx=npfromto(k,sx+dx,sy,tx,ty)
        ly=npfromto(k,sx,sy+dy,tx,ty)
        ret=[]
        for l in lx:
            if not "*" in l:
                ret.append(dxm+l)
        for l in ly:
            if not "*" in l:
                ret.append(dym+l)
        return ret

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

#        print("nftl",r,"A",sols)
#        if t=="A":
#            return sols
        s=t
        if not keys:
            return sols
        t=keys.pop(0)


for li in inp:
    print("l",li)
    l=list(li)

    # gjenta N ganger:
    #   gjør, for alle *A: (første omgang: kun 1)
    #       finn moves som passer for klumpen
    #   bygg beste struktur(er) for neste runde
    #   defaultdict er fint. 
    
    res1=moves(numk,nump,l)
    res1sorted=sorted(list(res1),key=len)
    blen=len(res1sorted[0])
    print("mmm",res1)
    r1i=0
    res2=set()
    while r1i<len(res1sorted) and len(res1sorted[r1i]) == blen:
        r2=moves(arrk,arrp,list(res1sorted[r1i]))
        print("r1",r1i,len(res1sorted[r1i]),res1sorted[r1i])
        for rrr in r2:
            print("  r2:",len(rrr),rrr)
        res2 = res2 | r2
#        print("rrr2",len(res2))
        r1i+=1

    rsort=sorted(list(res2),key=len)
    blen=len(rsort[0])
    for i in range(len(rsort)):
        print("rs1",i,rsort[i].count("A"),len(rsort[i]),rsort[i])
    res=set()
    ri=0
    while ri<len(rsort) and len(rsort[ri]) == blen:
#        print("r2",ri,len(rsort[ri]))
        r3=moves(arrk,arrp,list(rsort[ri]))
        res = res | r3
        print("r3",len(rsort[ri]),rsort[ri])
        for r4 in r3:
            print("   r4:",len(r4),r4)
#        print("rrr3",len(res))
        ri+=1

    rsort=sorted(list(res),key=len)
    blen=len(rsort[0])
    print("bll",blen,len(rsort))
    for i in range(min(len(rsort),40)):
        print("rs2",i,rsort[i].count("A"),len(rsort[i]),rsort[i])
    for i in range(len(rsort)-10,len(rsort)):
        print("rs2",i,rsort[i].count("A"),len(rsort[i]),rsort[i])
    print("lli",li[:-1])
    p1+=blen*int(li[:-1])

#    exit()
    # res=set()
    # ri=0
    # while ri<1 and ri<len(rsort) and len(rsort[ri]) == blen:
    #     print("r3",ri,len(rsort[ri]))
    #     res = res | moves(arrk,arrp,list(rsort[ri]))
    #     print("rrr4",len(res))
    #     ri+=1


#    for r2 in res2: #second arrow keypad
#         res3=moves(arrk,arrp,list(r2))
#         print("rrr3",len(res3))
    # for r3 in res3: # third arrow keypad
    #     res4=moves(arrk,arrp,list(r3))
    #     print("rrr4",len(res3))


print("1:",p1)
print("2:",p2)
