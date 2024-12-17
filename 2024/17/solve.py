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

ip=0 # inwstruction pointer

print("regs,p",rega,regb,regc,program)





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

    out=[]
    ip=0
    while ip < len(program):
        opcode=program[ip]
        operand=int(program[ip+1])
#        print("dd",opcode,operand,rega,regb,regc,ip)
        match str(opcode):
            case "0": #adv
                rega = rega // (2 ** combo(operand))
                ip+=2
            case "1": #bxl
                regb=regb ^ operand
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
                regb=regb ^ regc
                ip+=2
            case "5": #out
                out.append(str(combo(operand)%8)) # +","
#                print("oo",out,operand,combo(operand))
                ip+=2
            case "6": #bdv
                regb = rega // (2 ** combo(operand))
                ip+=2
            case "7": #cdv
                regc = rega // (2 ** combo(operand))
                ip+=2
    return ",".join(out)

# 375364177 wrong
# 627231605 wrong

p1=runit(program,rega,regb,regc)

print("1:",p1)

pp=",".join(program)
print("pp",pp)

# observasjon: lengde output stiger med størrelse input. start med å gange med 10 til vi har passe lengde:
p2=1
while(len(runit(program,p2,regb,regc))<len(pp)):
    p2*=2
    print("rr",p2,pp,runit(program,p2,regb,regc))

p2=p2//2


while runit(program,p2,regb,regc) != pp:
    p2+=1
    print("rr",p2,pp,runit(program,p2,regb,regc))

print("2:",p2)
# 1 000 000 000 too low
# 37 592 207 023 419 too low.. (?)
