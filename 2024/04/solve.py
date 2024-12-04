import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

map=[]
for l in inp:
    map.append(list(l))

p1=0
p2=0

w=len(map)
h=len(map[0])
# check hor:

for y in range(len(map)):
    ystr=""
    for x in range(len(map[y])):
        ystr+=map[y][x]

    p1+=ystr.count("XMAS")
    p1+=ystr.count("SAMX")
    ddstr=""
    sx=0
    sy=y
    if(sy>0):
        while sy<h and sx<w:
            ddstr+=map[sy][sx]
            sy+=1
            sx+=1
        p1+=ddstr.count("XMAS")
        p1+=ddstr.count("SAMX")

    ddstr=""
    sx=0
    sy=y
    if(sy<h-1):
        while sy>=0 and sx<w:
            ddstr+=map[sy][sx]
            sy-=1
            sx+=1
        p1+=ddstr.count("XMAS")
        p1+=ddstr.count("SAMX")

for x in range(len(map[0])):
    xstr=""
    for y in range(len(map)):
        xstr+=map[y][x]

    p1+=xstr.count("XMAS")
    p1+=xstr.count("SAMX")

    ddstr=""
    sx=x
    sy=0
    while sy<h and sx<w:
        ddstr+=map[sy][sx]
        sy+=1
        sx+=1
    p1+=ddstr.count("XMAS")
    p1+=ddstr.count("SAMX")

    ddstr=""
    sx=x
    sy=h-1
    while sy>=0 and sx<w:
        ddstr+=map[sy][sx]
        sy-=1
        sx+=1
    p1+=ddstr.count("XMAS")
    p1+=ddstr.count("SAMX")


for x in range(1,len(map[0])-1):
    for y in range(1,len(map)-1):
        if(map[y][x]=="A"):
            if (((map[y-1][x-1]=="M" and map[y+1][x+1]=="S") or
                 (map[y-1][x-1]=="S" and map[y+1][x+1]=="M")) and
                ((map[y+1][x-1]=="M" and map[y-1][x+1]=="S") or
                 (map[y+1][x-1]=="S" and map[y-1][x+1]=="M"))):
                p2+=1


print("1:",p1)
print("2:",p2)
