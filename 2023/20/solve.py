import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    input = [(s.split(" -> ")[0],s.split(" -> ")[1]) for s in f.read().strip().split("\n")]

print("i",input)

class inst:
    def __init__(self,name,t,targets,n,inp):
        self.name=name
        self.t=t
        self.targets=targets
        self.ninputs=n
        self.inputstate={}
        if(n>0):
            self.inputstate[inp]=False
        self.outputstate=False
        self.outputset=True

    def inp(self,source,pulse):
#        print("input",self.name,source,pulse,self.outputstate,self.outputset)
        self.inputstate[source]=pulse
        if(self.t=="%"):
            if(not pulse):
                self.outputstate = not self.outputstate
                self.outputset=True
            else:
                self.outputset=False
        elif(self.t=="&"):
            self.outputstate=not all(self.inputstate.values())
#            print("nand",self.inputstate,self.outputstate)
        elif(self.t=="b"):
            self.outputstate=pulse
        else:
            print("END!!")
#        print("output",self.name,self.outputstate,self.outputset)


insts={}

for l in input:
    tt=l[1].split(", ")
    if(l[0][0]=="%"):
        insts[l[0][1:]]=inst(l[0][1:],l[0][0],tt,0,"")
    elif(l[0][0]=="&"):
        insts[l[0][1:]]=inst(l[0][1:],l[0][0],tt,0,"")
    else:
        insts[l[0]]=inst(l[0],"b",tt,1,"bell")



xx=""
for i in insts.values():
    for tt in i.targets:
        if(tt in insts.keys()):
            insts[tt].ninputs+=1
            insts[tt].inputstate[i.name]=False
        else:
            xx=tt
            xxn=i.name
            
if(xx!=""):
    insts[xx]=inst(xx,"o",[],1,xxn)          

#for i in insts.values():
#    print("ffi",i.name,"t:",i.t,"targets",i.targets,"inputs",i.ninputs,i.inputstate)
        
def printstate():
    for inn in insts:
        i=insts[inn]
        print("i",i.name," inputs:",end="")
        for iss in i.inputstate:
            print(" ",iss,end="")
        print(" out",i.outputstate," outset",i.outputset)


def round(ii):
    q=[insts[ii]]
    while q:
        inst=q.pop(0)
        print("qloop",inst.name,len(q))

        for t in inst.targets:
            insts[t].inp(inst.name,inst.outputstate)
#            print("oset",t,inst.outputstate)
            if(insts[t].outputset):
                q.append(insts[t])
        
def run(ii,inp,val):        
    insts[ii].inp(inp,val)            
    printstate()
    round(ii)
    printstate()
    print("r2")
    round(ii)
    printstate()


run("broadcaster","bell",False)



print("1:", s1)
    
print("2:", s2)

