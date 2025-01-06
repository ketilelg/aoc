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
    #returns movestring(s) from sx,sy to tx,ty
#    print("nf",sx,sy,tx,ty)
    if k[sy][sx]=="*":
        return["*"]
    retstr=""
#    if sx==tx: #up/down:
#        print(" UD")
    if sx>tx:
        retstr+="<"*abs(sx-tx)
    if sx<tx: #r
        retstr+=">"*abs(tx-sx)
    if sy<ty:
        retstr+="^"*abs(ty-sy)
    if sy>ty:
        retstr+="v"*abs(sy-ty)
    return retstr

def numfromto(k,n,f,t):
    return(npfromto(k,n[f][0],n[f][1],n[t][0],n[t][1]))           

def moves(k,n,keys):
    # return best  possible way to achieve keys.. keys is list of keys
    s="A"
    t=keys.pop(0)
#    print("sdf",keys,s,t)
    sol=""
    while True:
        r=numfromto(k,n,s,t)
#        print(" fff",r,keys,s,t)
        sol+=r+"A"
#        print("  fs",s)

#        print("nftl",r,"A",sols)
#        if t=="A":
#            return sols
        s=t
        if not keys:
            return sol
        t=keys.pop(0)

# def moves(k,n,keys):
#     # return best  possible way to achieve keys.. keys is list of keys
#     s="A"
#     t=keys.pop(0)
#     print("sdf",keys,s,t)
#     sols={""}
#     while True:
#         r=numfromto(k,n,s,t)
#         ii=sols.copy()
#         print(" fff",r,ii,keys,s,t)
#         for s in ii:
#             for rr in r:
#                 print(" frr",rr,sols)
#                 nnn=s+rr+"A"
#                 print("  fs",nnn,s,rr,sols)
#                 sols.add(nnn)
#             sols.remove(s)

# #        print("nftl",r,"A",sols)
# #        if t=="A":
# #            return sols
#         s=t
#         if not keys:
#             return sols
#         t=keys.pop(0)


for li in inp:
    print("l",li)
    l=list(li)
    res1=moves(numk,nump,l)

    # for r in res1:
    #     moveset=defaultdict(int)
    #     pmoves=re.findall(r"([<>v^]*A)",r)
    #     print("---\n",r,"\n")
    #     for pm in pmoves:
    #         print("pm",pm)
    #         moveset[pm]+=1

    #     kpos="A"
    #     nextset=defaultdict(int)
    #     for mm in moveset:
    #         #mm in now string, ends with "A". may have moves in front. 
    #         nm=moveset[mm] #number of intances of this move..
    #         print("mmmmm",mm,nm)
            # match mm:
            #     case "A":
            #         nextset["A"]+=1
            #     case "<A":
            #         nextset["v<<A"]+=1
            #         nextset[">>^A"]+=1
            #     case ">A":
            #         nextset["vA"]+=1
            #         nextset["^A"]+=1
            #     case "^A":
            #         nextset["<A"]+=1
            #         nextset[">A"]+=1
            #     case "vA":
            #         nextset["<vA"]+=1
            #         nextset["A^>"]+=1
            #     case "v<<A":

    print("mmm",res1)

#    blen=len(rsort[0])
#    for i in range(0,128):
#        print("rs1",i,rsort[i].count("A"),len(rsort[i]),rsort[i],re.findall(r"([<>v^]*A)",rsort[i]))
#    res=set()
#    ri=0
#    while ri<len(rsort) and len(rsort[ri]) == blen:
#        print("r2",ri,len(rsort[ri]))
    res2=moves(arrk,arrp,list(res1))
    print("rrr",res2)

    res3=moves(arrk,arrp,list(res2))
    print(li,res3)


#     rsort=sorted(list(res),key=len)
    blen=len(res3)
#     print("bll",blen,len(rsort))
#     for i in range(0,10):
#         print("rs2",i,rsort[i].count("A"),len(rsort[i]),rsort[i])
#     for i in range(len(rsort)-10,len(rsort)):
#         print("rs2",i,rsort[i].count("A"),len(rsort[i]),rsort[i])
    print("lli",li[:-1],blen)
    p1+=blen*int(li[:-1])

# #    exit()
#     # res=set()
#     # ri=0
#     # while ri<1 and ri<len(rsort) and len(rsort[ri]) == blen:
#     #     print("r3",ri,len(rsort[ri]))
#     #     res = res | moves(arrk,arrp,list(rsort[ri]))
#     #     print("rrr4",len(res))
#     #     ri+=1


# #    for r2 in res2: #second arrow keypad
# #         res3=moves(arrk,arrp,list(r2))
# #         print("rrr3",len(res3))
#     # for r3 in res3: # third arrow keypad
#     #     res4=moves(arrk,arrp,list(r3))
#     #     print("rrr4",len(res3))


print("1:",p1)
print("2:",p2)
