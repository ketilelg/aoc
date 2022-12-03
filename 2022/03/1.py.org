#!/usr/bin/python3

p1=0

with open('input') as f:
    for line in f:
        rs=line.strip()
        hl=int(len(rs)/2)
        hs=rs[:hl]
        ts=rs[hl:]
        print(hl,hs,ts)

        for c in hs:
           if c in ts:
               print("treff",c)
               break
        v=ord(c)
        if v>96:
            v-=96
        if v>64:
            v-=38
        print("v",v)
        p1+=v

print("p1:",p1)
