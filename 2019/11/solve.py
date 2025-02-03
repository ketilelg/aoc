import sys
from collections import defaultdict

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))


p1=p2=0

pp=defaultdict(int)

for i,c in enumerate(inp):
    pp[i] = c

dirs={"<":(-1,0),"^":(0,-1),">":(1,0),"v":(0,1)}
ldir={"<":"v",
      "^":"<",
      ">":"^",
      "v":">"}
rdir={"<":"^",
      "^":">",
      ">":"v",
      "v":"<"}
posx=0
posy=0
dir="^"
cmap=defaultdict(tuple)

def printmap():
    minx=maxx=miny=maxy=0
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
            if x==posx and y==posy:
                print(dir,end="")
            elif (x,y) in cmap:
                if cmap[(x,y)]==1:
                    print("#",end="")
                else:
                    print(".",end="")
            else:
                print(" ",end="")
        print("")

def run(prog):
    global posx,posy,dir,cmap
    output=[]
    outstate=0 #for now: 0 or 1
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
                prog[paddr(params%10,prog[pc+1])]=cmap[(posx,posy)]
#                 if input:
#                     prog[paddr(params%10,prog[pc+1])]=input.pop()
# #                    print("input",prog[parm(params%10,prog[pc+1])],params,relbase,prog[pc+1],parm(params%10,prog[pc+1]))
# #                    print("ppp",prog)
#                 else:
#                     print("missing input",pc,opcode,params)
#                     exit()
#                print("input",prog[pc+1],prog[prog[pc+1]])
                pc+=2
            case 4: #output
                print("out:",parm(params%10,prog[pc+1]),outstate)
#                output.append(parm(params%10,prog[pc+1]))
                if outstate==0:
                    if parm(params%10,prog[pc+1]) == 1:
                        cmap[(posx,posy)]=1
                    else:
                        cmap[(posx,posy)]=0
                    outstate=1
                elif outstate==1: #turn and move
                    if parm(params%10,prog[pc+1]) == 1:
                        #turn left
                        dir=ldir[dir]
                    else:
                        #turn right
                        dir=rdir[dir]
                    dx,dy=dirs[dir]
                    posx+=dx
                    posy+=dy
                    outstate=0
                pc+=2
                printmap()
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

run(pp)

p1=len(cmap)

# sum(cmap.values())

print("1:",p1)
# 101 too low

print("2:",p1)