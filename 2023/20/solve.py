import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    input = [(s.split(" -> ")[0],s.split(" -> ")[1]) for s in f.read().strip().split("\n")]

print("i",input)

class inst:
    def __init__(self,name,t,targets,n):
        self.name=name
        self.t=t
        self.targets=targets
        self.ninputs=n

insts={}

for l in input:
    tt=l[1].split(", ")
    if(l[0][0]=="%"):
        insts[l[0][1:]]=inst(l[0][1:],l[0][0],tt,0)
    elif(l[0][0]=="&"):
        insts[l[0][1:]]=inst(l[0][1:],l[0][0],tt,0)
    else:
        insts[l[0]]=inst(l[0],"",tt,0)

insts["rx"]=inst("rx","end",[],0)

for i in insts.values():
    print("pfi",i.name,"t:",i.t,"targets",i.targets,"inputs",i.ninputs,type(i.ninputs))

for i in insts.values():
    print("fi",i.name,"t:",i.t,"targets",i.targets,"inputs",i.ninputs,type(i.ninputs))
    for tt in i.targets:
        print("itt",tt)
        insts[tt].ninputs+=1

for i in insts.values():
    print("ffi",i.name,"t:",i.t,"targets",i.targets,"inputs",i.ninputs)
        
def build(ii):
    inst=input[ii]
    for i in inst.split(","):
        i=i.strip()
        print("i",i)
        build(i)


def run(ii):
    inst=input[ii]
    for i in inst.split(","):
        i=i.strip()
        print("i",i)
        
    
#build("broadcaster")



print("1:", s1)
    
print("2:", s2)

