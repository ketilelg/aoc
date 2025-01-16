import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


for b in inp:
    double=False
    for p in range(1,len(b)):
        if b[p]==b[p-1]:
            double=True
    nw=b.count("a") +  b.count("e") + b.count("i") + b.count("o") + b.count("u")
    ok =  b.count("ab")==0 and b.count("cd")==0 and b.count("pq")==0 and b.count("xy")==0
    if double and nw>=3 and ok:
        p1+=1
print("1:",p1)
print("2:",p2)
