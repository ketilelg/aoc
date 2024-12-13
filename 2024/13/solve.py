import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    machines = f.read().strip().split("\n\n")


p1=p2=0

def presses(a,b,res):
    if(b*3 > a): #b most expensive
        na=nb=rr=0
        found=False
        rr=(-1,-1)
        while(not found and na*a<res):
            if (res-(na*a))%b == 0:
                print("hit",na,(res-na*a)//b)
                # result!
                found=True
                rr=(na,(res-na*a)//b)
            else:
                na+=1
        return(rr)
    else:
        na=nb=rr=0
        found=False
        rr=(-1,-1)
        while(not found and nb*b<res):
            if (res-(nb*b))%a == 0:
                print("hit",nb,(res-nb*b)//a)
                # result!
                found=True
                rr=((res-nb*b)//a,nb)
            else:
                nb+=1
        return(rr)
            



for m in machines:
    res=re.findall("\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)",m)
    ax,ay,bx,by,px,py=map(int,res[0])

    

print("sdf",presses(94,22,8400))
print("sdf",presses(17,84,7870))

print("1:",p1)
print("2:",p2)
