import re
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    hashes =  f.read().strip().split(",")

print("h",hashes)

def chash(h):
    v=0
    for c in h:
        v+=ord(c)
        v*=17
        v=v%256
    return v

def nhash(h):
    v=0
    for c in h[0],h[1]:
        v+=ord(c)
        v*=17
        v=v%256
    return v



n=0
boxes=[[] for s in range(256)]

sps=re.compile("=-")

for h in hashes:
    n+=1
    s1+=chash(h)
    np=nhash(h)
    if(h[-2]=="="):
        label=h[:-2]
        #is it there?
        found=False
        for p,l in enumerate(boxes[np]):
            if(l[:-2] == label):
                print("found",label,p)
                boxes[np][p] = label+" "+h[-1]
                found=True
        if(not found):
            print("new",label)
            boxes[np].append(label+" "+h[-1])
    else:
        label=h[:-1]
        print("remove",label)
        for p,l in enumerate(boxes[np]):
            if(l[:-2] == label):
                print("rfound",label,p)
                boxes[np].pop(p)
#    print("bbb",boxes[:10])

print("b",boxes)


print("n",n)
    
print("1:", int(s1))


for boxno,b in enumerate(boxes):
    for slotno,l in enumerate(b):
        print("bc",(boxno+1), slotno+1, int(l[-1]))
        s2+= (boxno+1) * (slotno+1) * int(l[-1])
    

print("2:", int(s2))
# 31163 too low
# 253561 too high
# 10015691 too high
