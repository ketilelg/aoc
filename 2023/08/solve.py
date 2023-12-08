import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    inst,nn = f.read().strip().split("\n\n")

net={}
for l in nn.split("\n"):
    node,rest=l.split(" = ")
    nl,nr=rest.split(", ")
    nl=nl[1:]
    nr=nr[:-1]
    net[node]={"L":nl,"R":nr}

pos="AAA"
steps=0
done=0
while not done:
    for c in inst:
        steps+=1
        pos=net[pos][c]
        if(pos=="ZZZ"):
            done=1
            break

        
        
print("1:", steps)

allsteps=[]

for pos in net:
    if(pos[2]=="A"):
        steps=0
        done=0
        while not done:
            for c in inst:
                steps+=1
                pos=net[pos][c]
                if(pos[2]=="Z"):
                    done=1
                    break
        allsteps.append(steps)
    
print("2:", math.lcm(*allsteps))

