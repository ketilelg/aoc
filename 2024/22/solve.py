import sys
from functools import cache
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) > 1) else 'input') as f:
    inp = list(map(int,f.read().strip().split("\n")))
            
def solve(num,gens):
    for i in range(gens):
        num= 16777215 & ((num<<6)^num) 
        num= 16777215 & ((num>>5)^num)
        num= 16777215 & ((num<<11)^num)
    return num        

def gencstr(num):
    #returns changestr, and matching pricelist for a given num
    iters=0
    chstrs={} # defaultdict(int)

    changes="" #-9=a, -8=b, etc
    prices=[num%10]

    while iters<2000:
        pnum=num
        num= 16777215 & ((num<<6)^num)
        num= 16777215 & ((num>>5)^num)
        num= 16777215 & ((num<<11)^num)
        ones=num%10
        pones=pnum%10
        changes = changes + chr(107+(ones-pones))
        if iters>=4:
            if not changes[iters-4:iters] in chstrs:
                chstrs[changes[iters-4:iters]]=pones
        prices.append(ones)
        iters+=1
    
    return num,changes,prices,chstrs

p1=p2=0
p2r=[]
changes=[]
prices=[]
css=defaultdict(int)
for n in inp:
#    p1+=solve(n,2000)
    n,c,p,cs=gencstr(n)
    changes.append(c)
    prices.append(p)
    for ccc in cs:
        css[ccc]+=cs[ccc]

p2=max(css.values())

print("1:",p1)
print("2:",p2)
