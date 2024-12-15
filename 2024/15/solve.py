import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    f1,f2 = f.read().strip().split("\n\n")

rmap=list(map(list,f1.split("\n")))
dirs=list(re.findall(r"([<>v^])",f2))
bmap=list(list(l.replace(".","..").replace("#","##").replace("@","@.").replace("O","[]")) for l in f1.split("\n"))

p1=p2=0

def printmap(m):
    for l in m:
        for c in l:
            print(c,end="")
        print("")

h=len(rmap)-1
w=len(rmap[0])-1

robx=roby=0
for x in range(w):
    for y in range(h):
        if rmap[y][x]=="@":
            robx=x
            roby=y
brobx=robx*2
broby=roby

print("rxy",robx,roby)

dv={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}

def ismovable(bmap,sx,sy,move):
    if bmap[sy][sx] == "[":
        return (ismovable(bmap,sx+dv[move][0],sy+dv[move][1],move) and 
                (move in "<>" or ismovable(bmap,sx+dv[move][0]+1,sy+dv[move][1],move)))
    elif bmap[sy][sx] == "]":
        return (ismovable(bmap,sx+dv[move][0],sy+dv[move][1],move) and 
                (move in "<>" or ismovable(bmap,sx+dv[move][0]-1,sy+dv[move][1],move)))
    elif bmap[sy][sx] == "O":
        return ismovable(bmap,sx+dv[move][0],sy+dv[move][1],move)
    elif bmap[sy][sx] == ".":
        return True
    return False

def movetree(bmap,ssx,ssy,sx,sy,move):
    # assumes movability
    if move in "^v":
        if bmap[sy][sx] == "[":
            movetree(bmap,ssx,ssy,sx+dv[move][0]+1,sy+dv[move][1],move)
        elif bmap[sy][sx] == "]":
            movetree(bmap,ssx,ssy,sx+dv[move][0]-1,sy+dv[move][1],move)
    if bmap[sy][sx] in "@[]O":
        movetree(bmap,ssx,ssy,sx+dv[move][0],sy+dv[move][1],move)
    if bmap[sy][sx] in "." and (ssx!=sx or ssy!=sy):
        oo=bmap[sy][sx]
        bmap[sy][sx] = bmap[sy-dv[move][1]][sx-dv[move][0]]
        bmap[sy-dv[move][1]][sx-dv[move][0]] = oo

for move in dirs:
    sx=robx+dv[move][0]
    sy=roby+dv[move][1]
    if ismovable(rmap,sx,sy,move):
        movetree(rmap,robx,roby,robx,roby,move)
        roby+=dv[move][1]
        robx+=dv[move][0]

    sx=brobx+dv[move][0]
    sy=broby+dv[move][1]
    if ismovable(bmap,sx,sy,move):
        movetree(bmap,brobx,broby,brobx,broby,move)
        broby+=dv[move][1]
        brobx+=dv[move][0]

for x in range(w):
    for y in range(h):
        if rmap[y+1][x+1]=="O":
            p1+=(100*(y+1))+x+1


for x in range(len(bmap[0])-1):
    for y in range(h):
        if bmap[y+1][x+1]=="[":
            p2+=(100*(y+1))+x+1


print("1:",p1)
print("2:",p2)
