import sys
import copy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    map = list(map(list,f.read().strip().split("\n")))

p1=0
p2=0

xmap=copy.deepcopy(map)
w=len(map)
h=len(map[0])

def printmap():
    for y in range(h):
        for x in range(w):
            print(map[y][x],end="")
        print("")

for y in range(w):
    for x in range(h):
        if(map[y][x]=="^"):
            posx=x
            posy=y

sposx,sposy=posx,posy

diry=-1
dirx=0

done=False
while not done:
    if map[posy][posx] != "X":
        map[posy][posx]="X"
        p1+=1
    posx+=dirx
    posy+=diry
    if(posy < 0 or posy >= h or posx < 0 or posx >= w):
        done=True
    else:
        if map[posy][posx] == "#":
            posx-=dirx
            posy-=diry
            if dirx==0:
                diry,dirx = 0, -diry
            else:
                dirx,diry = 0, dirx

omap=copy.deepcopy(map)
map=copy.deepcopy(xmap)

for y in range(h):
    for x in range(w):
        posx,posy=sposx,sposy
        om=map[y][x]
        map[y][x]="#"
        diry=-1
        dirx=0
        been=[]
        print("been",x,y)
        #vi prøver bare om det er sjanse for kollisjon:
        done = omap[y][x] in ["^",".","#"]
        while not done:
            posx+=dirx
            posy+=diry
            if(posy < 0 or posy >= h or posx < 0 or posx >= w):
                done=True
            elif (posx,posy,dirx,diry) in been:
                #loop, har vært her.
                print("loop",posx,posy,dirx,diry)
                p2+=1
                done=True
            else:
                if map[posy][posx] == "#":
                    been.append((posx,posy,dirx,diry))
                    posx-=dirx
                    posy-=diry
                    if dirx==0:
                        diry,dirx = 0, -diry
                    else:
                        dirx,diry = 0, dirx
        map[y][x]=om




print("xy",posx,posy)



print("1:",p1)
print("2:",p2)
