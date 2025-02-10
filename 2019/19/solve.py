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

def printmap(mmap):
    for l in mmap:
        for p in l:
            print(p,end="")
        print("")    

def run(prog,input):
    output=[]
#    posx=posy=0
#    dmap[(0,0)]=0
#    moves=0
#    dir="^"
#    ostr=""

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
                output.append(outval)
#                return output
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





cols=rows=200
mmap = [[0 for i in range(cols)] for j in range(rows)]

for x in range(cols):
    for y in range(rows):
        pp=defaultdict(int)
        for i,c in enumerate(inp):
            pp[i] = c

        ret=run(pp,[x,y])
        mmap[y][x]=ret[0]
        p1+=ret[0]

printmap(mmap)

print("1:",p1) 

pp=defaultdict(int)
for i,c in enumerate(inp):
    pp[i] = c

pp[0]=2

run(pp,list(map(ord,list("A,B,A,B,C,C,B,A,C,A\nL,10,R,8,R,6,R,10\nL,12,R,8,L,12\nL,10,R,8,R,8\nn\n"))))
