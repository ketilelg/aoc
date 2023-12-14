import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    mirror =  [list(s)for s in f.read().strip().split("\n")]

h=len(mirror)
w=len(mirror[0])

def printmirror(m):
    print()
    for l in m:
        for c in l:
            print(c,end="")
        print()


for c in range(w):
    nmoves=1
    while nmoves>0:
        nmoves=0
        for d in range(1,h):
            if((mirror[d][c]=="O") and (mirror[d-1][c]==".")):
                mirror[d][c]="."
                mirror[d-1][c]="O"
                nmoves+=1

               

def cycle(m):
    #north:
    for c in range(w):
        nmoves=1
        while nmoves>0:
            nmoves=0
            for d in range(1,h):
                if((m[d][c]=="O") and (m[d-1][c]==".")):
                    m[d][c]="."
                    m[d-1][c]="O"
                    nmoves+=1
    #west:
    for d in range(h):
        nmoves=1
        while nmoves>0:
            nmoves=0
            for c in range(1,w):
                if((m[d][c]=="O") and (m[d][c-1]==".")):
                    m[d][c]="."
                    m[d][c-1]="O"
                    nmoves+=1
    #south:
    for c in range(w):
        nmoves=1
        while nmoves>0:
            nmoves=0
            for d in range(h-2,-1,-1):
                if((m[d][c]=="O") and (m[d+1][c]==".")):
                    m[d][c]="."
                    m[d+1][c]="O"
                    nmoves+=1
    #east:
    for d in range(h):
        nmoves=1
        while nmoves>0:
            nmoves=0
            for c in range(w-2,0-1,-1):
                if((m[d][c]=="O") and (m[d][c+1]==".")):
                    m[d][c]="."
                    m[d][c+1]="O"
                    nmoves+=1

def stringify(m):
    r=""
    for l in m:
        r=r+"".join(l)
    return r

def count(m):
    res=0
    for c in range(w):
        for r in range(h):
            if(m[r][c]=="O"):
                res+=(h-r)
    return(res)

s1=count(mirror)


print("1:", int(s1))

pm=dict()

round=0

# print("str",stringify(mirror))
mstr=stringify(mirror)
while not mstr in pm:
    pm[mstr]=round
    round+=1
    cycle(mirror)
    mstr=stringify(mirror)
    print("round",round,count(mirror),mstr)


    
print("urkurk",round,100 % (round-pm[mstr]),pm[mstr])    
print("2:", int(s2))

