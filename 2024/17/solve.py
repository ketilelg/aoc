import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(f.read().strip().split("\n"))

rega=regb=regc=0

for l in inp:
    if "Register A" in l:
        rega=int(l.split(": ")[1])
    elif "Register B" in l:
        regb=int(l.split(": ")[1])
    elif "Register C" in l:
        regc=int(l.split(": ")[1])
    elif "Program" in l:
        program=list(l.split(": ")[1].split(","))

p1=""
p2=0

def runit(program,rega,regb,regc):
    def combo(op):
        if op < 4: 
            return op
        if op == 4: 
            return rega
        if op == 5: 
            return regb
        if op == 6: 
            return regb
        if op == 7:
            print("illegal combo op")
            exit()

    out=""
    ip=0
    while ip < len(program):
        opcode=program[ip]
        operand=int(program[ip+1])
#        print("dd",program,opcode,operand,rega,regb,regc,ip)
        match str(opcode):
            case "0": #adv
                rega = rega // (2 ** combo(operand))
                ip+=2
            case "1": #bxl
                regb=int(regb) ^ int(operand)
                ip+=2
            case "2": #bst
                regb=combo(operand) % 8
                ip+=2
            case "3": #jnz
                if rega!=0:
                    ip=operand
                else:
                    ip+=2
            case "4": #bxc
                regb=int(regb) ^ int(regc)
                ip+=2
            case "5": #out
                out=out+str(combo(operand)%8)
                ip+=2
            case "6": #bdv
                regb = rega // (2 ** combo(operand))
                ip+=2
            case "7": #cdv
                regc = rega // (2 ** combo(operand))
                ip+=2
    return out

p1=runit(program,rega,regb,regc)

print("1:",",".join(p1))

pp="".join(program)

def rlmatch(s1,s2):
    mm=0
    f=False
    while mm < len(s1) and mm<len(s2) and s1[-(mm+1):]==s2[-(mm+1):]:
        mm+=1
        f=True
    return mm

p2=1
step=1

tpr=""
pl=len(pp)
step=1
p2=0
while tpr!= pp:
    p2+=step
    tpr=runit(program,p2,regb,regc)
    ml=rlmatch(pp,tpr)
    tl=len(tpr)
    step=2**(3*(tl-ml-1))
#    print("rr",p2,pp,"-",tpr,"-",len(tpr),rlmatch(pp,tpr))

print("2:",int(p2))
