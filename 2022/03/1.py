#!/usr/bin/python3

p1=0

with open('input') as f:
    for line in f:
        rs=line.strip()
        hl=int(len(rs)/2)

        c=''.join(set(rs[:hl]).intersection(set(rs[hl:])))

        v=ord(c)
        if v>96:
            v-=96
        if v>64:
            v-=38

        p1+=v

print("p1:",p1)
