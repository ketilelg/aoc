import sys
import re
import numpy as np

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    machines = f.read().strip().split("\n\n")


p1=p2=0

def npresses(ax,bx,ay,by,resx,resy):
    # 2 equations, 2 unknowns..:
    A=np.array([[ax,bx],
                [ay,by]])
    y = np.array([resx,resy])
    x=np.linalg.solve(A,y)
    a=round(x[0],3) #teh ugly, because finite precision
    b=round(x[1],3)
    if(a.is_integer() and b.is_integer()):
        return int(a)*3 + int(b)
    else:
        return 0



for m in machines:
    ax,ay,bx,by,resx,resy=map(int,re.findall(r"\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)",m)[0])
    p1+=npresses(ax,bx,ay,by,resx,resy)
    p2+=npresses(ax,bx,ay,by,resx+10000000000000,resy+10000000000000)

print("1:",p1)
print("2:",p2)
