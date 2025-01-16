import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0
p2notfonund=True
frq=set()

for c in inp:
    p1=eval("p1"+c)
#        print("p1",p1)
    if p1 in frq:
        p2=p1
        p2notfonund=False
        break
    frq.add(p1)

print("1:",p1)

while p2notfonund:
    for c in inp:
        p1=eval("p1"+c)
#        print("p1",p1)
        if p1 in frq:
            p2=p1
            p2notfonund=False
            break
        frq.add(p1)

print("2:",p2)
