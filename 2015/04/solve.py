import sys
import hashlib

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=p2=0

n=0
while True:
    tstr=inp+str(n)
    out=hashlib.md5(tstr.encode()).hexdigest()
    if out[:5]=="00000":
        print("found it",tstr,out)
        break
    n+=1


print("1:",inp+str(n))
print("2:",p2)
