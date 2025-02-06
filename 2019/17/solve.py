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
# cmap=defaultdict(str)
# dmap=defaultdict(int) #shortest walk from start
smap=[]

def printmap():
    for i,l in enumerate(smap):
        print(i,":",l,"<-")

def printmapxx():
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
            elif (x,y) in cmap:
                print("████",end="")
            else:
                print("....",end="")
        print("")


def run(prog,input):
    global smap,p1
    output=[]
#    posx=posy=0
#    dmap[(0,0)]=0
#    moves=0
#    dir="^"
    ostr=""

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
                if input:
                    prog[paddr(params%10,prog[pc+1])]=input.pop(0)
#                printmap()
#                prog[paddr(params%10,prog[pc+1])]=0 # dirc[dir]
#                print("input!")
#                print("in:",posx,posy,params%10,prog[pc+1],cmap[(posx,posy)])
                pc+=2
            case 4: #output
#                print("out:",parm(params%10,prog[pc+1]))
#                output.append(parm(params%10,prog[pc+1]))
                outval=parm(params%10,prog[pc+1])
                if outval==10:
                    print("out:",ostr,"<-")
#                    if ostr=="":
#                        printmap()
#                        smap=[]
                    smap.append(ostr)
                    ostr=""
                elif outval < 256:
                    ostr+=chr(outval)
#                    print("oo",ostr)
                else:
                    print("final out",outval)
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

run(pp,[])

smap.pop()
printmap()

for y in range(1,len(smap)-1):
    for x in range(1,len(smap[0])-1):
#        print("xy",x,y)
        if smap[y][x]=="#" and smap[y-1][x]=="#" and smap[y+1][x]=="#" and smap[y][x-1]=="#" and smap[y][x+1]=="#":
            print("inter",x,y)
            p1+=(x)*(y)


print("1:",p1) 

pp=defaultdict(int)
for i,c in enumerate(inp):
    pp[i] = c

pp[0]=2

run(pp,list(map(ord,list("A,B,A,B,C,C,B,A,C,A\nL,10,R,8,R,6,R,10\nL,12,R,8,L,12\nL,10,R,8,R,8\nn\n"))))
