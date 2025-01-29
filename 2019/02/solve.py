import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


p1=p2=0


def run(prog):
    pc=0
    while pc<len(prog):
        match prog[pc]:
            case 1:
                prog[prog[pc+3]]=prog[prog[pc+2]]+prog[prog[pc+1]]
                pc+=4
            case 2:
                prog[prog[pc+3]]=prog[prog[pc+2]]*prog[prog[pc+1]]
                pc+=4
            case 99:
                pc=len(prog)

inp[1]=12
inp[2]=2
run(inp)
print("1:",inp[0])
print("2:",p2)
