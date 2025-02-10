import sys
from collections import defaultdict
import itertools

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


p1=p2=0


def run(prog,input,pc,relbase):
#    print("run..",prog,input,pc,relbase)
    output=[]
#    pc=0
#    relbase=0
    def parm(mode,param):
#        print("parm",mode,param)
        if mode==0:
            return prog[param]
        elif mode==1:
            return param
        elif mode==2:
            return prog[param+relbase]
        else:
            print("illegal param")
            exit()

    def paddr(mode,param):
#        print("parm",mode,param)
        if mode==0:
            return param
        elif mode==1:
            print("can't do that")
            exit()
        elif mode==2:
            return param+relbase
        else:
            print("illegal param")
            exit()


    while pc<len(prog):
        params=prog[pc]//100
        opcode=prog[pc]%100
#        print("w",pc,opcode,params)
        match opcode:
            case 1: #add
#                print("add",pc,opcode,params,prog[pc+3],parm(params%10,prog[pc+1]),parm((params//10) % 10,prog[pc+2]))
                prog[paddr((params//100)%10,prog[pc+3])]=parm(params%10,prog[pc+1])+parm((params//10) % 10,prog[pc+2])
                pc+=4
            case 2: #mul
                prog[paddr((params//100)%10,prog[pc+3])]=parm(params%10,prog[pc+1])*parm((params//10) % 10,prog[pc+2])
                pc+=4
            case 3: #input
                if input:
                    ipp=input.pop(0)
                    prog[paddr(params%10,prog[pc+1])]=ipp
#                    print("input",ipp) #prog[parm(params%10,prog[pc+1])],params,relbase,prog[pc+1],parm(params%10,prog[pc+1]))
#                    print("ppp",prog)
                else:
                    print("missing input",pc,opcode,params)
                    exit()
#                print("input",prog[pc+1],prog[prog[pc+1]])
                pc+=2
            case 4: #output
                outval=parm(params%10,prog[pc+1])
#                print("out:",outval)
                output.append(parm(params%10,prog[pc+1]))
                pc+=2
                return outval,pc,relbase
            case 5: #jmpift
                if parm(params%10,prog[pc+1]) != 0:
                    pc=parm((params//10) % 10,prog[pc+2])
                else:
                    pc+=3
            case 6: #jmpiff
                if parm(params%10,prog[pc+1]) == 0:
                    pc=parm((params//10) % 10,prog[pc+2])
                else:
                    pc+=3
            case 7: #lt
                if parm(params%10,prog[pc+1]) < parm((params//10) % 10,prog[pc+2]):
                    prog[paddr((params//100)%10,prog[pc+3])]=1
                else:
                    prog[paddr((params//100)%10,prog[pc+3])]=0
                pc+=4
            case 8: #eq
                if parm(params%10,prog[pc+1]) == parm((params//10) % 10,prog[pc+2]):
                    prog[paddr((params//100)%10,prog[pc+3])]=1
                else:
                    prog[paddr((params//100)%10,prog[pc+3])]=0
                pc+=4
            case 9: #relbase
                relbase+=parm(params%10,prog[pc+1])
                pc+=2
            case 99: #halt
                pc=len(prog)
                return -1,0,0
#        print("sdf",prog)            
    return output

combs=[[3,1,2,4,0]]
for c in itertools.permutations([0,1,2,3,4]):
    out=0
    for ph in c:

        pp=defaultdict(int)
        for i,c in enumerate(inp):
            pp[i] = c
        
        ip=[ph,out]
#        print("ip",ip)
        out,pc,relb=run(pp,ip,0,0)
#        print("outtt",out)
    if out>p1:
        p1=out


print("1:",p1) 

for c in itertools.permutations([5,6,7,8,9]):
    out=0
    running=True
    pc=[]
    relbase=[]
    prog=[]
    ip=[]
    for j,ph in enumerate(c):
        ip.append([ph,0])
        pc.append(0)
        relbase.append(0)
        prog.append(defaultdict())
        pp=defaultdict(int)
        for i,c in enumerate(inp):
            prog[j][i] = c
        # should be setup by here. 
    p=0 #which machine?
    while running:
        out,pc[p],relbase[p]= run(prog[p],ip[p],pc[p],relbase[p])
#        print("rr",out,p)
        p+=1
        if p>=len(pc):
            p=0
            if out>p2:
                p2=out
#        print("ipip",ip,out,p)
        if ip[p]:
            ip[p][-1]=out
        else:
            ip[p]=[out]
#        print("ipip2",ip,out,p)
        if out==-1:
            running=False



print("2:",p2)