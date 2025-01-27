import sys
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

def runit():
    regs=defaultdict(int)
    pc=0
    while pc<len(inp):
        op=inp[pc][:3]
        rh=inp[pc][4:]
        match op:
            case "hlf":
                regs[rh]=int(regs[rh]/2)
                pc+=1
            case "tpl":
                regs[rh]*=3
                pc+=1
            case "inc":
                regs[rh]+=1
                pc+=1
            case "jmp":
                pc+=int(rh)
            case "jie":
                reg,off=rh.split(", ")                    
                if regs[reg]%2==0:
                    pc+=int(off)
                else:
                    pc+=1
            case "jio":
                reg,off=rh.split(", ")                    
                if regs[reg]==1:
                    pc+=int(off)
                else:
                    pc+=1
#    print("rr",regs)
    return regs["b"]

print("1:",runit())
inp.insert(0,"inc a")
print("2:",runit())
