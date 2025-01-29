import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


p1=p2=0

pp=inp.copy()

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

pp[1]=12
pp[2]=2
run(pp)
print("1:",pp[0])

for n in range(100):
    for v in range(100):
        pp=inp.copy()
        pp[1]=n
        pp[2]=v
        run(pp)
        if pp[0]==19690720:
            print("2:",n,v,(100*n)+v)

print("2:",p2)
