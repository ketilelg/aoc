import sys
from functools import cache

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

@cache
def timelines(l,p):
    global p1
    if (l+1)==len(inp): #veis ende, ikke noe mer å hente
        return 1
    else:
        if inp[l+1][p]=="^":
            p1+=1 #sideeffekt i cachede rekursive funksjoner. <3
            return timelines(l+1,p-1) + timelines(l+1,p+1)
        else:
            return timelines(l+1,p)

p2=timelines(0,inp[0].find("S"))        

print("1:",p1)
print("2:",p2)
