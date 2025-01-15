import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=p2=0

p1=inp.count("(")-inp.count(")")

l=0
p=1
for c in inp:
    if c=="(":
        l+=1
    elif c==")":
        l-=1
    if l==-1:
        p2=p
        break
    p+=1
print("1:",p1)
print("2:",p2)
