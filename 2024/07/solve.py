import sys
from itertools import product

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0
for line in inp:
    left,eq=line.split(": ")
    ff=eq.split(" ")
    allops=product(["+","*","||"],repeat = len(ff)-1)
    for opers in list(allops):
        factors=ff.copy()
        ops=list(opers)
        result=int(factors.pop(0))
        while len(factors)>0:
            op=ops.pop(0)
            if op=="||":
                result=int(str(result)+factors.pop(0))
            elif op=="+":
                result+=int(factors.pop(0))
            elif op=="*":   
                result*=int(factors.pop(0))
        if(int(left)==result):
            p2+=result
            if "||" not in opers:
                p1+=result
            break

print("1:",p1)
print("2:",p2)