import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    map = f.read().strip().split("\n")

w=len(map[0])
h=len(map)

nmap=[[" "] *h*3 for _ in range(w*3)]



symbols={"-":["   ","***","   "],
         "|":[" * "," * "," * "],
         "7":["   ","** "," * "],
         "F":["   "," **"," * "],
         "J":[" * ","** ","   "],
         "L":[" * "," **","   "],
         "S":[" * ","***"," * "]}
         

#find start:
for x in range(w):
    for y in range(h):
        if(map[y][x]=="S"):
            sx=x
            sy=y
    

def floop(sx,sy,dir,dist):
    done=0
    nx=sx
    ny=sy
    me=map[sy][sx]
    #om vi starter:
    if((me=="S") and (dist == 0)):

        for xx in range(3):
            for yy in range(3):
                nmap[(sx*3)+xx][(sy*3)+yy] = symbols[me][yy][xx]

        dn=ds=dw=de=0
        if((sy>0) & (map[sy-1][sx] in "|7F")):
           dn=floop(sx,sy-1,"n",dist+1)
        if((sy<(h-1)) & (map[sy+1][sx] in "|JL")):
           ds=floop(sx,sy+1,"s",dist+1)
        if((sx>0) & (map[sy][sx-1] in "-FL")):
           dw=floop(sx-1,sy,"w",dist+1)
        if((sx<(w-1)) & (map[sy][sx+1] in "-J7")):
           de=floop(sx+1,sy,"e",dist+1)
        return(max(dn,ds,de,dw))
    elif(me in  "|-7FJL"):
        for xx in range(3):
            for yy in range(3):
                nmap[(sx*3)+xx][(sy*3)+yy] = symbols[me][yy][xx]
        if((dir=="n") and (me in "|7F")):
           if((sy > 0) and (me == "|")):
               return(floop(sx,sy-1,"n",dist+1))
           if((sx > 0) and (me == "7")):
               return(floop(sx-1,sy,"w",dist+1))
           if((sx < (w-1)) and (me == "F")):
               return(floop(sx+1,sy,"e",dist+1))
        elif((dir=="s") and (me in "|JL")):
           if((sy < h-1) and (me == "|")):
               return(floop(sx,sy+1,"s",dist+1))
           if((sx > 0) and (me == "J")):
               return(floop(sx-1,sy,"w",dist+1))
           if((sx < (w-1)) and (me == "L")):
               return(floop(sx+1,sy,"e",dist+1))
        elif((dir=="w") and (me in "-FL")):
           if((sx > 0) and (me == "-")):
               return(floop(sx-1,sy,"w",dist+1))
           if((sy < (h-1)) and (me == "F")):
               return(floop(sx,sy+1,"s",dist+1))
           if((sy > 0) and (me == "L")):
               return(floop(sx,sy-1,"n",dist+1))
        elif((dir=="e") and (me in "-J7")):
           if((sx < (w-1)) and (me == "-")):
               return(floop(sx+1,sy,"e",dist+1))
           if((sy < (h-1)) and (me == "7")):
               return(floop(sx,sy+1,"s",dist+1))
           if((sy > 0) and (me == "J")):
               return(floop(sx,sy-1,"n",dist+1))
        else:
            return(0)
    else:
        return(dist)
           
s1=int(floop(sx,sy," ",0)/2)

print("1:", s1)


nmap[0][0]="O"
nh=h*3
nw=w*3

def fill():
    n=1
    while(n > 0):
        n=0
        for x in range(nh):
            for y in range(nw):
                if(nmap[y][x] == " "):
                    if(((x-1>= 0) and (nmap[y][x-1]=="O")) or
                       ((x+1< nh) and (nmap[y][x+1]=="O")) or
                       ((y-1>= 0) and (nmap[y-1][x]=="O")) or
                       ((y+1< nw) and (nmap[y+1][x]=="O"))):
                        nmap[y][x]="O"
                        n+=1

fill()

for x in range(h):
    for y in range(w):
        if(nmap[(y*3)+1][(x*3)+1]==" "):
            s2+=1
            nmap[(y*3)+1][(x*3)+1]="I"


print("2:", s2)

