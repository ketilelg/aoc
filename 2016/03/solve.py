import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

for k in inp:
    sides=list(map(int,k.split()))
    sides.sort()
    if sides[0]+sides[1]>sides[2]:
        p1+=1


for i in range(int(len(inp)/3)):
    tsides=[]
    for j in range(3):
        tsides.append(list(map(int,inp[(i*3)+j].split())))
    for j in range(3):
        sides=[]
        for k in range(3):
            sides.append(int(tsides[k][j]))
        sides.sort()
        print("ss",sides)
        if sides[0]+sides[1]>sides[2]:
            p2+=1

print("1:",p1)
print("2:",p2)
