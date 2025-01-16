import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

def fuelcalc(w):
    f=max(int(int(w)/3)-2,0)
    if f>6:
        f+=fuelcalc(f)
    return f

for c in inp:
    p1+=int(int(c)/3)-2
    p2+=fuelcalc(int(c))
print("1:",p1)
print("2:",p2)
