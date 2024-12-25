import sys
import re
from functools import cache
from itertools import combinations

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    f1,f2 = f.read().strip().split("\n\n")

with open("scratch") as scratch:
    scd=scratch.read().strip().split("\n")
tests=set()
for ss in scd:
    print("ss",ss)
    l=ss.split(" ")
    tests.add((l[1],l[2]))

print("tests",tests)

p1=p2=0

#gtrans={}
wires={} #wires with known data. will grow as 
for l in f1.split("\n"):
    w,s=l.split(": ")
    wires[w]=int(s)
#    gtrans[w]=w

nbits=len(wires)//2
print("nbits",nbits)
gates={} #these are unknown state
#rgates={} #must be renamed
for l in f2.split("\n"):
    tt=re.findall(r"(.+)\s+(.+)\s+(.+)\s+->\s+(.+)",l)[0]
    gates[tt[3]]=(tt[0],tt[1],tt[2])
    # if (tt[0][0]=="x" or tt[0][0]=="y") and tt[1]=="AND" and tt[3][0]!="z":
    #     name="c"+tt[0][1:]
    #     gtrans[tt[3]]=name
    # elif (tt[0][0]=="x" or tt[0][0]=="y") and tt[1]=="XOR" and tt[3][0]!="z":
    #     name="v"+tt[0][1:]
    #     gtrans[tt[3]]=name
    # else:
    #     name=tt[3]
    #     gtrans[tt[3]]=tt[3]

#print("gt",gtrans)

# for l in f2.split("\n"):
#     tt=re.findall(r"(.+)\s+(.+)\s+(.+)\s+->\s+(.+)",l)[0]
#     gates[gtrans[tt[3]]]=(gtrans[tt[0]],tt[1],gtrans[tt[2]])


#print("gg",gates)    

#exit()


sgates={} #solved
visited=set()

def findv(g,verbose,ss):
    global visited
    #g is name of gate or wire, returns value.
    if verbose:
        print(ss,"findv",g)
    if g in visited:
        return -1
    if g in wires:

        return wires[g]
    else:
        visited.add(g)
        match gates[g][1]:
            case "AND":
                out = findv(gates[g][0],verbose,ss+" ") & findv(gates[g][2],verbose,ss+" ")
            case "OR":
                out = findv(gates[g][0],verbose,ss+" ") | findv(gates[g][2],verbose,ss+" ")
            case "XOR":
                out = findv(gates[g][0],verbose,ss+" ") ^ findv(gates[g][2],verbose,ss+" ")
        visited.remove(g)
        return out            


# while len(gates)>0:
#     print("www",len(gates),len(wires))
#     for g in list(gates):
#         if gates[g][0] in wires and gates[g][2] in wires:
#             match gates[g][1]:
#                 case "AND":
#                     out = wires[gates[g][0]] and wires[gates[g][2]]
#                 case "OR":
#                     out = wires[gates[g][0]] or wires[gates[g][2]]
#                 case "XOR":
#                     out = wires[gates[g][0]] != wires[gates[g][2]]
#             gates.pop(g)
# #            print("out",out)
#             wires[g]=out
# # print("ww",wires)

for i in gates:
    if i[0]=="z":
        if findv(i,False,"") == 1:
            p1 += 2**(int(i[1:]))

print("p1",p1)
print("")

wires={}

def nfaults(verbose): #return number of faults, given this set of gates
    nfaults=0
    fbits=[]
    for xb in range(nbits): 
        p2=0
        for i in range(nbits):
            wires["x"+f"{i:02d}"]=1 if xb==i else 0
            wires["y"+f"{i:02d}"]=0
        for i in gates:
            if i[0]=="z":
                if findv(i,False,"")==1:
                    p2+= 2**(int(i[1:]))
        if p2 != 2**xb:
            if verbose:
                print("xx",xb,p2,2**xb)
            fbits.append(xb)
            nfaults+=1
    return nfaults,fbits

nf,fb=nfaults(True)
print("nf",nf,fb)
if nf>0:
#     for g1,g2 in combinations(tests,2):
#         gates[g1],gates[g2]=gates[g2],gates[g1]
#         tnf,tfb=nfaults(False)
# #        print("cc",g1,g2,tnf,tfb)
#         if tnf<nf:
#             print("hoi",g1,g2,tnf,nf,tfb)
#             t2=tests.copy()
#             t2.remove(g1)
#             t2.remove(g2)
#             for g3,g4 in combinations(t2,2):
#                 gates[g3],gates[g4]=gates[g4],gates[g3]
#                 tnf2,tfb2=nfaults(False)
# #                print("cc",g3,g4,tnf2,tfb2)
#                 if tnf2<tnf:
#                     print("hoihoi",g1,g2,g3,g4,tnf,tfb2)
#                 gates[g3],gates[g4]=gates[g4],gates[g3]
#         gates[g1],gates[g2]=gates[g2],gates[g1]
    for p in combinations(tests,4):
        for pp in p:
            gates[pp[0]],gates[pp[1]]=gates[pp[1]],gates[pp[0]]
        tnf,tfb=nfaults(False)
#        print("cc",p,tnf,tfb)
        if tnf==0:
            print("hoi",p,tnf,nf,tfb)
        for pp in p:
            gates[pp[0]],gates[pp[1]]=gates[pp[1]],gates[pp[0]]
        

# for xb in range(nbits): 
#     p2=0
#     for i in range(nbits):
#         wires["x"+f"{i:02d}"]=1 if xb==i else 0
#         wires["y"+f"{i:02d}"]=0
#     for i in gates:
#         if i[0]=="z":
#             if findv(i,False,"")==1:
#                 p2+= 2**(int(i[1:]))
#     if p2 != 2**xb:
#         print("xx",xb,p2,2**xb)
#         nfaults+=1


print(" ")

# wires={}
# for yb in range(nbits): 
#     p2=0
#     for i in range(nbits):
#         wires["y"+f"{i:02d}"]=1 if yb==i else 0
#         wires["x"+f"{i:02d}"]=0
#     for i in gates:
#         if i[0]=="z":
#             if findv(i,False,"")==1:
#                 p2+= 2**(int(i[1:]))
#     if p2!= 2**yb:
#         print("yx",yb,p2,2**yb)

#print("ww",wires)