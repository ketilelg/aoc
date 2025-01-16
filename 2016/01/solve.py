import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split(", ")

p1=p2=0

visits=set()
dir=0 #0 is north
x=y=0
for c in inp:
    t=c[0]
    d=int(c[1:])
    if t=="L":
        dir-=90
    elif t=="R":
        dir+=90
    else:
        print("wtf")
    if dir<0:
        dir+=360
    if dir>=360:
        dir=dir%360
    for dd in range(d):
        match dir:
            case 0:
                y+=1
            case 90:
                x+=1
            case 180:
                y-=1
            case 270:
                x-=1
        if (x,y) in visits:
            p2=abs(x)+abs(y)
            print("2:",p2,x,y)
        visits.add((x,y))
        

    print("ccc",c,t,dir,x,y)


print("xy",x,y)
p1=abs(x)+abs(y)


print("1:",p1)
print("2:",p2)
