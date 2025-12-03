import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

def  joltage(n,sifre):
    j=0    
    spos=0
    for i in range(n-1,-1,-1):
        epos=len(sifre)-i
        sif=(max(sifre[spos:epos]))
        j*=10
        j+=sif
        spos=sifre[spos:].index(sif)+1+spos
    return j

for l in inp:
    sifre=list(map(int,list(l)))
    p1+=joltage(2,sifre)
    p2+=joltage(12,sifre)

print("1:",p1)
print("2:",p2)
