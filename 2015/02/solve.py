import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


for b in inp:
    print("b",b)
    bs=list(map(int,b.split("x")))
    bs.sort()
    print("bb",bs)
    area=(bs[0]*bs[1]*3)+(bs[0]*bs[2]*2)+(bs[1]*bs[2]*2)
    p1+=area
    bow=(bs[0]*2)+bs[1]*2+(bs[0]*bs[1]*bs[2])
    p2+=bow
    
print("1:",p1)
print("2:",p2)
