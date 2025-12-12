import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n\n")

p1=p2=0

shapes=[]
for l in inp[:-1]:
    print("l",l.split("\n"))
    shapes.append(list(map(list,l.split("\n")[1:])))

print("ss",shapes)
for rl in inp[-1].split("\n"):
    w,h=map(int,rl.split(":")[0].split("x"))
    q=list(map(int,rl.split(": ")[1].split(" ")))
    
    sq=sum(q)
    a3=(w//3)*(h//3)
    if a3>=sq:
        p1+=1
    else:
        print("cc",w,h,sq,a3)

print("1:",p1)
print("2:",p2)
