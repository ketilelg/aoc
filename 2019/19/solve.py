import sys
from collections import defaultdict
from functools import cache

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(map(int,f.read().strip().split(",")))

p1=p2=0

smap=[]

def printmap(mmap):
    for l in mmap:
        for p in l:
            print(p,end="")
        print("")    

def run(prog,input):
    output=[]

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
                pc+=2
            case 4: #output
#                print("out:",parm(params%10,prog[pc+1]))
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
    return output

cols=50
rows=50
start=0
end=cols


def findse(y):
    global start,end
    #return start, end of line at y. (start=first 1, end=first 0)
    prev=0
    for x in range(start-1,start+2):
        pp=defaultdict(int)
        for i,c in enumerate(inp):
            pp[i] = c
        ret=run(pp,[x,y])[0]
        if prev==0 and ret==1:
#            print("stst",x)
            start=x
            prev=1
    for x in range(end-2,end+2):
        pp=defaultdict(int)
        for i,c in enumerate(inp):
            pp[i] = c
        ret=run(pp,[x,y])[0]
        if prev==1 and ret==0:
#            print("ee",x)
            end=x
            prev=0
    return start,end

mmap = [[0 for i in range(cols)] for j in range(rows)]
its=0
start=0
end=cols
for y in range(rows):
    prev=0
    for x in range(start,min(cols,end+3)):
        pp=defaultdict(int)
        for i,c in enumerate(inp):
            pp[i] = c
        ret=run(pp,[x,y])[0]
        its+=1
#        print("pp",prev,ret)
        if prev==0 and ret==1:
#            print("stst",x)
            start=x
        if prev==1 and ret==0:
#            print("ee",x)
            end=x
        prev=ret
        mmap[y][x]=ret
        if y<50:
            p1+=ret
#    print("start,end",y,start,end)    

printmap(mmap)
print("its",its,start,end)
print("1:",p1) 

found=False
y=rows
ends={}
while not found:
    start,end=findse(y)
    ends[y]=end
#    print("se",y,start,end)
    if end-start>=100:
        if ends[y-99]>=start+100:
            found=True
    y+=1

print("se",start,end,ends[y-100])
print("2: ",(start*10000)+y-100)