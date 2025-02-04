import sys
from collections import defaultdict
import os

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


dirs={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}
dirc={"<":3,"^":1,">":4,"v":2}
ldir={"<":"v",
      "^":"<",
      ">":"^",
      "v":">"}
rdir={"<":"^",
      "^":">",
      ">":"v",
      "v":"<"}


p1=p2=0
cmap=defaultdict(str)
dmap=defaultdict(int) #shortest walk from start

def printmap():
    print('\033c', end='')
    minx=maxx=miny=maxy=0
#    print("pm",cmap)
    for c in cmap:
        x,y=c
        if x < minx:
            minx=x
        if x > maxx:
            maxx=x
        if y < miny:
            miny=y
        if y > maxy:
            maxy=y
    print("mm",minx,maxx,miny,maxy,len(cmap))
    for y in range(miny-1,maxy+2):
        for x in range(minx-1,maxx+2):
            if (x,y) in cmap:
                print(cmap[(x,y)],end="")
            else:
                print(".",end="")
        print("")

    for y in range(miny-1,maxy+2):
        for x in range(minx-1,maxx+2):
            if (x,y) in dmap:
                print(f'{dmap[(x,y)]:4d}',end="")
            else:
                print("....",end="")
        print("")


def run(prog):
    global cmap,dmap,p1
    output=[]
    posx=posy=0
    dmap[(0,0)]=0
    moves=0
    dir="^"

    pc=0
    relbase=0
    def parm(mode,param):
#        print("parm",mode,param)
        if mode==0:
            return prog[param]
        elif mode==1:
            return param
        elif mode==2:
            return prog[param+relbase]
        else:
            print("illegal param")
            exit()

    def paddr(mode,param):
#        print("parm",mode,param)
        if mode==0:
            return param
        elif mode==1:
            print("can't do that")
            exit()
        elif mode==2:
            return param+relbase
        else:
            print("illegal param")
            exit()


    while pc<len(prog):
        params=prog[pc]//100
        opcode=prog[pc]%100
#        print("w",pc,opcode,params)
        match opcode:
            case 1: #add
#                print("add",pc,opcode,params,prog[pc+3],parm(params%10,prog[pc+1]),parm((params//10) % 10,prog[pc+2]))
                prog[paddr((params//100)%10,prog[pc+3])]=parm(params%10,prog[pc+1])+parm((params//10) % 10,prog[pc+2])
                pc+=4
            case 2: #mul
                prog[paddr((params//100)%10,prog[pc+3])]=parm(params%10,prog[pc+1])*parm((params//10) % 10,prog[pc+2])
                pc+=4
            case 3: #input
                prog[paddr(params%10,prog[pc+1])]=dirc[dir]
#                print("in:",posx,posy,params%10,prog[pc+1],cmap[(posx,posy)])
                pc+=2
            case 4: #output
#                print("out:",parm(params%10,prog[pc+1]),outstate)
#                output.append(parm(params%10,prog[pc+1]))
                outval=parm(params%10,prog[pc+1])
                if outval==0: #hit wall
                    dx,dy=dirs[dir]
                    cmap[(posx+dx,posy+dy)]="█"
                    #turn right
                    dir=rdir[dir]
#                    printmap()
                elif outval==1: #moved
                    dx,dy=dirs[dir]
                    moves=dmap[(posx,posy)]
                    posx+=dx
                    posy+=dy
                    if (posx,posy) in dmap:
                        moves=min(moves,dmap[(posx,posy)])
                    else:
                        moves+=1
                        dmap[(posx,posy)]=moves
                    cmap[(posx,posy)]=dir
                    if (posx+dx,posy+dy) in cmap:
                        dir=ldir[dir]
#                    printmap()
                    print("mm",moves)
                elif outval==2: #moved, hit
                    dx,dy=dirs[dir]
                    posx+=dx
                    posy+=dy
                    cmap[(posx,posy)]="2"
                    cmap[(0,0)]="S"
                    printmap()
                    print("oxy at ",posx,posy,moves)
                    p1=moves+1
                    pc=len(prog)
                pc+=2
            case 5: #jmpift
                if parm(params%10,prog[pc+1]) != 0:
                    pc=parm((params//10) % 10,prog[pc+2])
                else:
                    pc+=3
            case 6: #jmpiff
                if parm(params%10,prog[pc+1]) == 0:
                    pc=parm((params//10) % 10,prog[pc+2])
                else:
                    pc+=3
            case 7: #lt
                if parm(params%10,prog[pc+1]) < parm((params//10) % 10,prog[pc+2]):
                    prog[paddr((params//100)%10,prog[pc+3])]=1
                else:
                    prog[paddr((params//100)%10,prog[pc+3])]=0
                pc+=4
            case 8: #eq
                if parm(params%10,prog[pc+1]) == parm((params//10) % 10,prog[pc+2]):
                    prog[paddr((params//100)%10,prog[pc+3])]=1
                else:
                    prog[paddr((params//100)%10,prog[pc+3])]=0
                pc+=4
            case 9: #relbase
                relbase+=parm(params%10,prog[pc+1])
                pc+=2
            case 99: #halt
                pc=len(prog)
#        print("sdf",prog)            
    return output




pp=defaultdict(int)
for i,c in enumerate(inp):
    pp[i] = c


run(pp)



print("1:",p1)

#should do fill here. found answer manually. 

print("2:",302) #478 too high. 302 right. 
