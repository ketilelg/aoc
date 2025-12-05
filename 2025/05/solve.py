import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n\n")

fresh=inp[0].split("\n")
avail=map(int,inp[1].split("\n"))

p1=p2=0


for i in avail:
    ff=False
    for f in fresh:
        s,e=map(int,f.split("-"))
        if (i >=s) and (i <=e):
            ff=True
            break
    if ff:
        p1+=1

nf=[] # ny, forbedret liste. har aldri overlapp
for f in fresh: #legg til en og en, men ikke så det blir overlapp:
    s,e=map(int,f.split("-")) #plukk et nytt intervall fra original liste
    nnf=[]
    for i in range(len(nf)): #sjekk det nye med allerede lagrede intervaller i den nye liste
        (ns,ne)=nf[i]
        if (e<ns) or (s>ne): #de overlapper ikke
            pass
        elif (s<=ns) and (e>=ne): #den nye er større enn den gamle
            nf[i]=(-1,-1)
        elif (s>=ns) and (e<=ne): #den gamle er større enn den nye
            s=e=-1
            break
        elif (s<=ns) and (e>=ns): #overlapp 
            e=ns-1
        elif (s>=ns) and (e>=ne): #overlapp
            s=ne+1
    if (s>=0) and (e>=0):
        nf.append((s,e))

for t in nf:
    if (t[1]>=0) and (t[0]>=0):
        p2+=t[1]-t[0]+1
        
print("1:",p1)
print("2:",p2)
