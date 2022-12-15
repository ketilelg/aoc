#!/usr/bin/python3

import re

f=open('input')
lines=f.readlines()
sxa=[]
sya=[]
bxa=[]
bya=[]

for l in range(len(lines)):
    sx,sy,bx,by = map(int,re.findall(r'-?\d+',lines[l]))
#    print("ss",sx,sy,bx,by)
    sxa.append(sx)
    sya.append(sy)
    bxa.append(bx)
    bya.append(by)

def linecover(lineno,sx,sy,bx,by):
    size=abs(sx-bx)+abs(sy-by)
    dist=abs(lineno-sy)
    if dist<size:
        return (sx-size+dist),(sx+size-dist)
    else:
        return 0,-1
        
def overlap(lineno):
    overl=[]
    for yy in range(len(sxa)):
        s,e=linecover(lineno,sxa[yy],sya[yy],bxa[yy],bya[yy])
        if e >= s:
#            print("over",s,e,sxa[yy],sya[yy],bxa[yy],bya[yy])
            overl.append([s,e])
            
#            print("overl",overl)
            overl.sort()
#            print("overl",overl)
            sx=overl[0][0]
            se=overl[0][1]
            sumcover=se-sx+1
            for line in overl:
                sumcover+=max(line[1]-max(line[0],se),0)
                se=max(se,line[1])
#                print("fl",line,se,sumcover)
    return sumcover

def hole(lineno):
    overl=[]
    for yy in range(len(sxa)):
        s,e=linecover(lineno,sxa[yy],sya[yy],bxa[yy],bya[yy])
        if e >= s:
#            print("over",s,e,sxa[yy],sya[yy],bxa[yy],bya[yy])
            overl.append([s,e])
#            print("overl",overl)
    overl.sort()
#    print("overl",overl)
    sx=overl[0][0]
    se=overl[0][1]
    sumcover=se-sx+1
    for line in overl:
#        print("flo",se,line[0])
        if line[0] > se+1:
#            print("overl",overl)
#            print("hepp",lineno,line[0],se)
            return se+1
        else:
            se=max(line[1],se)
    return -1


print("p1, remove beacons!",overlap(2000000))


for l in range(4000000):
    r=hole(l)
#    if l%10000 == 0:
#        print("l",l)
#    print("ll",l,r)

    if r > 0:
        p2=r*4000000+l
        break
    
print("p2:",p2)
