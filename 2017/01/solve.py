import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=p2=0


p=inp[-1:]
l=len(inp)
h=int(l/2)
for i in range(l):
    c=inp[i]
    if c==p:
        p1+=int(c)
    if c==inp[(i+h)%l]:
        p2+=int(c)
    p=c
print("1:",p1)
print("2:",p2)
