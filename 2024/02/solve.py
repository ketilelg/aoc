import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

levels=[]
for li in inp:
    levels.append(list(map(int,li.split(" "))))
p1=0
p2=0

for l in levels:
    up=l[0]<l[1]
    ok=True
    for i in range(len(l)-1):
        ok=ok and (((1 <= l[i] - l[i+1] <= 3) and not up) or 
                   ((1 <= l[i+1] - l[i] <= 3) and up))
    if ok:
        p1 = p1 + 1
    if not ok:
        ok=False
        for j in range(len(l)):
            lp=l.copy()
            lp.pop(j)
            ook=True
            for i in range(len(lp)-1):
                up=lp[0]<lp[1]
                ook=ook and (((1 <= lp[i] - lp[i+1] <= 3) and not up) or 
                            ((1 <= lp[i+1] - lp[i] <= 3) and up))
            ok=ok or ook
        if ok:
            p2 = p2 + 1

print("1:",p1)
print("2:",p2+p1)
