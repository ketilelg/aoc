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

posx=-1
posy=-1
for y in range(w):
    for x in range(h):
        if(map[y][x]=="^"):
            posx=x
            posy=y

sposx,sposy=posx,posy

diry=-1
dirx=0

printmap()
print()

done=False
while not done:
    if map[posy][posx] != "X":
        map[posy][posx]="X"
        p1+=1
    posx+=dirx
    posy+=diry
#    printmap()
    print("dxdy",dirx,diry)
    if(posy < 0 or posy >= h or posx < 0 or posx >= w):
#        print("dd",posx,posy,w,h)
        done=True
    else:
        if map[posy][posx] == "#":
            posx-=dirx
            posy-=diry
            if dirx==0:
                diry,dirx = 0, -diry
            else:
                dirx,diry = 0, dirx

for y in range(h):
    for x in range(w):
        posx,posy=sposx,sposy
        map=copy.deepcopy(xmap)
        map[y][x]="#"
        diry=-1
        dirx=0
        been=[[(0,0)] * w  for j in range(h)] 

        print("been",x,y)
        done = (x==sposx) and (y==sposy)
        while not done:
            been[posy][posx]=(dirx,diry)
#            print("BBB1",x,y,posx,posy,been[posy][posx],(dirx,diry))
            posx+=dirx
            posy+=diry
#            print("BBB",x,y,posx,posy,been[posy][posx],(dirx,diry))
#            printmap()
#            print("dxdy",dirx,diry)
            if(posy < 0 or posy >= h or posx < 0 or posx >= w):
#                print("dd",posx,posy,w,h)
                done=True
            elif been[posy][posx][0] == dirx and been[posy][posx][1]==diry:
                #loop, har vært her.
                print("been",posx,posy,dirx,diry)
                p2+=1
                done=True
            else:
                if map[posy][posx] == "#":
                    posx-=dirx
                    posy-=diry
                    if dirx==0:
                        diry,dirx = 0, -diry
                    else:
                        dirx,diry = 0, dirx





print("xy",posx,posy)



print("1:",p1)
print("2:",p2)
