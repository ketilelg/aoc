import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

ll=[]
rl=[]
for li in inp:
    l,r=li.split("   ")
    ll.append(int(l))
    rl.append(int(r))
ll.sort()
rl.sort()
d=0
dd=0
for i in range(len(ll)):
    d+=abs(ll[i]-rl[i])
    dd+=ll[i]*rl.count(ll[i])

print("1:",d)
print("2:",dd)
