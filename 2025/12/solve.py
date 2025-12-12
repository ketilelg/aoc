import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n\n")

p1=p2=0

for rl in inp[-1].split("\n"):
    w,h=map(int,rl.split(":")[0].split("x"))
    q=list(map(int,rl.split(": ")[1].split(" ")))
    
    sq=sum(q)
    a3=(w//3)*(h//3)
    if a3>=sq:
        p1+=1

print("1:",p1)
print("2:",p2)
