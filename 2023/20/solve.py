import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    input = {s.split(" -> ")[0] : s.split(" -> ")[1] for s in f.read().strip().split("\n")}

print("i",input)


def run(inst):
    inst=input[inst]
    for i in inst.split(","):
        i=i.strip()
        print("i",i)
        
    
run("broadcaster")
        
print("1:", s1)
    
print("2:", s2)

