#!/usr/bin/python3

import numpy as np

f=open('input')
jet=f.read().strip()

jetpos=-1



def nextjet():
    global jetpos
    jetpos=(jetpos+1)%len(jet)
    return jet[jetpos]


iters=2022
iters=1000000000000
# iters=5*len(jet)

rocks=[[["#","#","#","#"]],
       [[".","#","."],["#","#","#"],[".","#","."]],
       [["#","#","#"],[".",".","#"],[".",".","#"]],
       [["#"],["#"],["#"],["#"]],
       [["#","#"],["#","#"]]]

rocktype=0
#highest point in stack
highest=0
#lowest point in stack...??
lowest=0

stack=[[",",",",",",",",",",",",","]]

def printline(line):
        for i in range(len(stack[line])):
            print(stack[line][i],end="")
        print("",line)
    

def printstack():
    print("stack:")
    for j in range(len(stack)-1,-1,-1):
        printline(j)


def stops(rock,xpos,ypos,offset):
    # given rockno, x and ypos - does it collide with stack, walls or floor?
    if ypos<0 or xpos < 0 or xpos+len(rocks[rock%5][0]) > 7:
        return True
    for x in range(len(rocks[rock%5][0])):
        for y in range( min(len(rocks[rock%5]) , (highest-ypos)) ):
            if rocks[rock%5][y][x]=="#" and stack[(y+ypos)-offset][x+xpos]=="#":
                return True
    return False
                       
                   

jbpairs={"sdfsdf":0}
repfoundstart=False
repfoundend=False

i=0
#offset in stack, when we jump ahead..:
stackoff=0
#for i in range(iters):
while i < iters:
    if not repfoundend:
        jbp=str(jetpos)+"og"+str(i%5)
        x=jbpairs.get(jbp)
        if x!= None:
            x=x+1
        else:
            x=1
        jbpairs[jbp]=x
        if jbpairs[jbp]==2 and not repfoundstart:
            #we have a repeat..
            repfoundstart=True
            print("start jbp",i,jbp,jbpairs[jbp])
            repjp=jetpos
            reprock=i%5
            repstart=i
            repstarth=highest
        if jbpairs[jbp]==3 and not repfoundend:
            #repeat end. we skip ahead..:
            replen=i-repstart
            reph=highest-repstarth
            nreps=int((iters-i)/replen)-1
            repfoundend=True
            print("end jbp",i,jbp,jbpairs[jbp],nreps,replen,reph)
            i+=nreps*replen
            stackoff=nreps*reph
            highest+=stackoff
        
    moving=True
    xp=2
    yp=highest+3
    while moving:
        if nextjet() == "<":
            xp-=1
            if stops(i,xp,yp,stackoff):
                xp+=1
        else:
            xp+=1
            if stops(i,xp,yp,stackoff):
                xp-=1

        yp-=1
        if yp<highest:
            #now, a collision is possible
            if stops(i,xp,yp,stackoff):
                moving=False
                yp+=1

    for y in range(len(rocks[i%5])-(highest-yp)):

        stack.append([",",",",",",",",",",",",","])
        highest +=1
    for y in range(len(rocks[i%5])):
        for j in range(len(rocks[i%5][y])):
            if (rocks[i%5][y][j]) == "#":
                stack[(yp+y)-stackoff][xp+j]=(rocks[i%5][y][j])
    i+=1

#    printstack()


#printstack()

print("end",highest,iters)
