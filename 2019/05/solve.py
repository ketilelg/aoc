import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


p1=p2=0

pp=inp.copy()

def run(prog,input):
    pc=0

    def parm(mode,param):
#        print("parm",mode,param)
        if mode==0:
            return prog[param]
        elif mode==1:
            return param
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
                prog[prog[pc+3]]=parm(params%10,prog[pc+1])+parm((params//10) % 10,prog[pc+2])
                pc+=4
            case 2: #mul
                prog[prog[pc+3]]=parm(params%10,prog[pc+1])*parm((params//10) % 10,prog[pc+2])
                pc+=4
            case 3: #input
                prog[prog[pc+1]]=input.pop()
#                print("input",prog[pc+1],prog[prog[pc+1]])
                pc+=2
            case 4: #output
                print("out",params,pc+1,":",parm(params%10,prog[pc+1]))
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
                    prog[prog[pc+3]]=1
                else:
                    prog[prog[pc+3]]=0
                pc+=4
            case 8: #eq
                if parm(params%10,prog[pc+1]) == parm((params//10) % 10,prog[pc+2]):
                    prog[prog[pc+3]]=1
                else:
                    prog[prog[pc+3]]=0
                pc+=4
            case 99: #halt
                pc=len(prog)
#        print("sdf",prog)            


print("1:")
run(pp,[1])
pp=inp.copy()

print("2:")
run(pp,[5])
