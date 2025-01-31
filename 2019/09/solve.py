import sys
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


p1=p2=0

pp=defaultdict(int)

for i,c in enumerate(inp):
    pp[i] = c

def run(prog,input):
    output=[]
    pc=0
    relbase=0
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
                    prog[paddr(params%10,prog[pc+1])]=input.pop()
#                    print("input",prog[parm(params%10,prog[pc+1])],params,relbase,prog[pc+1],parm(params%10,prog[pc+1]))
#                    print("ppp",prog)
                else:
                    print("missing input",pc,opcode,params)
                    exit()
#                print("input",prog[pc+1],prog[prog[pc+1]])
                pc+=2
            case 4: #output
                print("out:",parm(params%10,prog[pc+1]))
                output.append(parm(params%10,prog[pc+1]))
                pc+=2
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
#        print("sdf",prog)            
    return output

print("1:",run(pp,[1])) #203 too low
# run(pp,[1])

pp=defaultdict(int)

for i,c in enumerate(inp):
    pp[i] = c

print("2:",run(pp,[2]))