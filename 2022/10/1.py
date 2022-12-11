#!/usr/bin/python3

regx=1
clock=0
p1=0
p2="\n"

def css():
    global regx,clock,p1
    if (clock-20)%40==0:
        p1+=regx*clock

def spc():
    global regx,clock,p2
    if ((regx-1) <= ((clock-1)%40)) and ((regx+1) >= ((clock-1)%40)):
        p2+="#"
    else:
        p2+="."
    if (clock%40 == 0):
        p2+="\n"

        
with open('input') as f:
    for line in f:
        if line.find("noop")>=0:
            clock += 1
            css()
            spc()
        elif line.find("addx")>=0:
            c,v=line.split()
            v=int(v)
            clock+=1
            css()
            spc()
            clock+=1
            css()
            spc()
            regx+=v
                
print("p1",p1,clock)
print("p2\n",p2)
