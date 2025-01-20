import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=0
p2=0

def cstr(istr):
    n=1
    c=istr[:1]
    istr=istr[1:]
    rstr=""
    while istr:
        nc=istr[:1]
        if c==nc:
            n+=1
        else:
            rstr+=str(n)+c

print("1:",p1)
print("2:",p2)
