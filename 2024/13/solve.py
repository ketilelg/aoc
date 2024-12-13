import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    machines = f.read().strip().split("\n\n")


p1=p2=0

def presses(ax,bx,ay,by,resx,resy):
    if(bx*3 > ax): #b most expensive
        na=nb=rr=0
        found=False
        rr=(-1,-1)
        while(not found and na*ax<resx):
            if (resx-(na*ax))%bx == 0 and (resy-(na*ay))%by==0:
#                print("hit",na,(resx-na*ax)//bx)
                # result!
                found=True
                rr=(na,(resx-na*ax)//bx)
            else:
                na+=1
        return(rr)
    else:
        na=nb=rr=0
        found=False
        rr=(-1,-1)
        while(not found and nb*bx<resx):
            if (resx-(nb*bx))%ax == 0 and (resy-(nb*by))%ay == 0:
#                print("hit",nb,(resx-nb*bx)//ax)
                # result!
                found=True
                rr=((resx-nb*bx)//ax,nb)
            else:
                nb+=1
        return(rr)
            



for m in machines:
    res=re.findall("\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)",m)
    ax,ay,bx,by,px,py=map(int,res[0])
    pp=presses(ax,bx,ay,by,px,py)
    print("ff",pp)
    if(pp!=(-1,-1)):
        p1+=(pp[0]*3)+pp[1]


print("1:",p1)
# 79660 too high. 
print("2:",p2)
