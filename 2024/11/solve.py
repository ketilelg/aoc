import sys
from functools import cache

with open(sys.argv[1] if (len(sys.argv) > 1) else 'input') as f:
    inp = list(map(int,f.read().strip().split(" ")))

@cache
def blink(num,gen):
    if(gen==0):
        return 1
    else:
        if num==0:
            return blink(1,gen-1)
        elif len(str(num))%2 == 0:
            return(blink(int(str(num)[:len(str(num))//2]),gen-1)+
                   blink(int(str(num)[len(str(num))//2:]),gen-1))
        else:
            return(blink(2024*num,gen-1))
            
def solve(gens):
    r=0
    for i in inp:
        r+=blink(i,gens)
    return r

print("1:",solve(25))
print("2:",solve(75))
