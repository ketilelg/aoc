import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    puzzle = f.read().strip().split("\n\n")

p1=0
plocks=[]
pkeys=[]
for p in puzzle:
    pl=p.split("\n")
    outl=[]
    iskey=pl[0][0]=="."
    for i in range(len(pl[0])): # per column
        v=0
        for j in range(len(pl)): # per line
            if iskey and pl[j][i]==".":
                v+=1
            elif not iskey and pl[j][i]=="#":
                v+=1
        outl.append(v-1)
    if iskey:
        pkeys.append(outl)
    else:
        plocks.append(outl)

for l in plocks:
    for k in pkeys:
        match=True
        for i in range(len(l)):
            match=match and l[i]<=k[i]
        if match:
            p1+=1

print("p1",p1)