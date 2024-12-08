import sys
import copy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    map = list(map(list,f.read().strip().split("\n")))

p1=0
p2=0

xmap=copy.deepcopy(map)
w=len(map)
h=len(map[0])

def printmap(m):
    for y in range(h):
        for x in range(w):
            print(m[y][x],end="")
        print("")

antennas={}
for y in range(w):
    for x in range(h):
        if  map[y][x] != ".":
            if map[y][x] not in antennas:
                antennas[map[y][x]]=[]
            antennas[map[y][x]].append((x,y))

antinodes={}
anti2={}
for antname in antennas:
    antlist=antennas[antname]
    for i in range(len(antlist)):
        anti2[antlist[i]]="@"
        for j in range(len(antlist)-i):
            if i!=j+i:
                (x1,y1)=antlist[i]
                (x2,y2)=antlist[j+i]
                dx=x2-x1
                dy=y2-y1
                nx1=x1-dx
                nx2=x2+dx
                ny1=y1-dy
                ny2=y2+dy
                if (nx1>=0 and nx1<w and ny1>=0 and ny1<h):
                    antinodes[(nx1,ny1)]="#"
                    while(nx1 >=0 and nx1< w and ny1>=0 and ny1 <h):
                        anti2[(nx1,ny1)]="#"
                        xmap[ny1][nx1]="#"
                        nx1-=dx
                        ny1-=dy

                if (nx2>=0 and nx2<w and ny2>=0 and ny2<h):
                    antinodes[(nx2,ny2)]="#"
                    while(nx2 >=0 and nx2< w and ny2>=0 and ny2 <h):
                        anti2[(nx2,ny2)]="#"
                        xmap[ny2][nx2]="#"
                        nx2+=dx
                        ny2+=dy
    
printmap(xmap)
p1=len(antinodes)
p2=len(anti2)

print("1:",p1)
print("2:",p2)
