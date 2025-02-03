import sys
from collections import defaultdict
import os

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


p1=p2=0
cmap=defaultdict(int)

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
                if cmap[(x,y)]>0:
                    print(cmap[(x,y)],end="")
                else:
                    print(".",end="")
            else:
                print(" ",end="")
        print("")

def run(prog):
    global cmap
    output=[]
    outstate=0 #0,1,2
    posx=posy=0
    bx=by=0 #ball position
    px=py=0 # paddle position 
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
                jdir=0
                if bx < px:
                    jdir=-1
                elif bx > px:
                    jdir=1
                prog[paddr(params%10,prog[pc+1])]=jdir
#                print("in:",posx,posy,params%10,prog[pc+1],cmap[(posx,posy)])
                pc+=2
            case 4: #output
#                print("out:",parm(params%10,prog[pc+1]),outstate)
#                output.append(parm(params%10,prog[pc+1]))
                outval=parm(params%10,prog[pc+1])
                if outstate==0:
                    posx=outval
                    outstate=1
                elif outstate==1:
                    posy=outval
                    outstate=2
                elif outstate==2: #graphics!
                    if (posx==-1 and posy==0):
                        print("score",outval)
                    else:
                        cmap[(posx,posy)]=outval
                        if outval==3:
                            px=posx
                            py=posy
                        elif outval==4:
                            bx=posx
                            by=posy
                    outstate=0
                    printmap()
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


p1=sum(filter(lambda x:x==2,cmap.values()))//2



print("1:",p1)

pp=defaultdict(int)
for i,c in enumerate(inp):
    pp[i] = c

pp[0]=2

run(pp)


print("2:",p2)