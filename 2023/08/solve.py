import math
import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    inst,nn = f.read().strip().split("\n\n")

net={}
for l in nn.split("\n"):
    node,rest=l.split(" = ")
    nl,nr=rest[1:-1].split(", ")
    net[node]={"L":nl,"R":nr}

def nsteps(pos):
    steps=0
    done=0
    while not done:
        for c in inst:
            steps+=1
            pos=net[pos][c]
            if(pos[2]=="Z"):
                done=1
                break
    return(steps)
                
print("1:", nsteps("AAA"))

print("2:", math.lcm(*list(map(nsteps,[pos for pos in net if pos[2] == "A"]))))
