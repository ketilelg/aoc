#!/usr/bin/python3

p1=0

f=open('input')
lines=f.readlines()

for l in range(0,len(lines),3):

    cs=set(lines[l].strip()).intersection(set(lines[l+1]).intersection(set(lines[l+2])))

    c=''.join(cs)

    v=ord(c)
    if v>96:
        v-=96
    if v>64:
        v-=38

    p1+=v

print("p1:",p1)
