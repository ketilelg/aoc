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
        p1=n
        break
    n+=1
while True:
    tstr=inp+str(n)
    out=hashlib.md5(tstr.encode()).hexdigest()
    if out[:6]=="000000":
        print("found it",tstr,out)
        p2=n
        break
    n+=1


print("1:",p1)
print("2:",p2)
