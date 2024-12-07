import sys
from itertools import product

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0
for li in inp:
    ll,eq=li.split(": ")
    ff=eq.split(" ")
    ops=product(["+","*","||"],repeat = len(ff)-1)
    for ooo in list(ops):
        factors=ff.copy()
        oo=list(ooo)
        newexp=int(factors.pop(0))
        while len(factors)>0:
            opp=oo.pop(0)
            if opp=="||":
                newexp=int(str(newexp)+factors.pop(0))
            elif opp=="+":
                newexp+=int(factors.pop(0))
            elif opp=="*":   
                newexp*=int(factors.pop(0))
            else:
                print("wtf???")        
        if(int(ll)==newexp):
            p2+=newexp
            if "||" not in ooo:
                p1+=newexp
            break

print("1:",p1)
print("2:",p2)