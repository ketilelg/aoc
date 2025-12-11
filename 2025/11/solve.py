import sys
from collections import defaultdict
import re
from functools import cache


with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

rack=dict()
for l in inp:
    st,en=l.split(": ")
    rack[st]=en.split(" ")

@cache
def paths(st,p1,fft,dac):
    n=0
    if st=="fft":
        fft=True
    elif st=="dac":
        dac=True
    for p in rack[st]:
        if p=="out":
#            print("out",fft,dac)
            if p1 or (fft and dac):
                return 1
            else:
                return 0
        else:
            n+=paths(p,p1,fft,dac)
    return n

p1=paths("you",True,False,False)
p2=paths("svr",False,False,False)
print("1:",p1)
print("2:",p2)
