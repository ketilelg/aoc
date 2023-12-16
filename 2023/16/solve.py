s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    mmap =  [list(s)for s in f.read().strip().split("\n")]

h=len(mmap)
w=len(mmap[0])

def printm(m):
    for l in m:
        for c in l:
            print(c,end="")
        print()


def bcount(sx,sy,sd):
    #map of beams, to avoid inf looops
    beams=[[set() for x in range(w)] for y in range(h)]

    def beamf(beams,x,y,d):
        #follow beam, starting at x,y, d (<>v^= as direction
        while((x >= 0) and (x < w) and (y >= 0) and (y < h) and not d in beams[y][x]):
            beams[y][x].add(d)
            if(mmap[y][x]=="."):
                if(d=="<"):
                    x-=1
                elif(d==">"):
                    x+=1
                elif(d=="^"):
                    y-=1
                elif(d=="v"):
                    y+=1
                else:
                    print("wut=")
            elif(mmap[y][x]=="|"):
                if((d=="<") or (d==">")):
                    beamf(beams,x,y-1,"^")
                    beamf(beams,x,y+1,"v")
                elif(d=="^"):
                    y-=1
                elif(d=="v"):
                    y+=1
                else:
                    print("wut=")
            elif(mmap[y][x]=="-"):
                if((d=="^") or (d=="v")):
                    beamf(beams,x+1,y,">")
                    beamf(beams,x-1,y,"<")
                elif(d=="<"):
                    x-=1
                elif(d==">"):
                    x+=1
                else:
                    print("wut=")
            elif(mmap[y][x]=="/"):
                if(d=="<"):
                    d="v"
                    y+=1
                elif(d==">"):
                    d="^"
                    y-=1
                elif(d=="^"):
                    d=">"
                    x+=1
                elif(d=="v"):
                    d="<"
                    x-=1
                else:
                    print("wut=")
            elif(mmap[y][x]=="\\"):
                if(d=="<"):
                    d="^"
                    y-=1
                elif(d==">"):
                    d="v"
                    y+=1
                elif(d=="^"):
                    d="<"
                    x-=1
                elif(d=="v"):
                    d=">"
                    x+=1
                else:
                    print("wut=")
            else:
                print("double wut",mmap[y][x],x,y)
                
    beamf(beams,sx,sy,sd)

    r=0
    for l in beams:
        for p in l:
            if(len(p)>0):
                r+=1
    return(r)

s1=bcount(0,0,">")

print("1:", s1)

for y in range(h):
    s2=max(s2,bcount(0,y,">"),bcount(w-1,y,"<"))
for x in range(w):
    s2=max(s2,bcount(x,0,"v"),bcount(x,h-1,"^"))

print("2:", int(s2))

