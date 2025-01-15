import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=p2=0

x=y=0
houses={(x,y)}
for c in inp:
    if c=="<":
        x-=1
    elif c==">":
        x+=1
    elif c=="^":
        y+=1
    elif c=="v":
        y-=1
    houses.add((x,y))

p1=len(houses)

rx=ry=x=y=0
houses={(x,y)}
santa=True
for c in inp:
    if santa:
        if c=="<":
            x-=1
        elif c==">":
            x+=1
        elif c=="^":
            y+=1
        elif c=="v":
            y-=1
        houses.add((x,y))
    else:
        if c=="<":
            rx-=1
        elif c==">":
            rx+=1
        elif c=="^":
            ry+=1
        elif c=="v":
            ry-=1
        houses.add((rx,ry))
    santa=not santa

p2=len(houses)

print("1:",p1)
print("2:",p2)
