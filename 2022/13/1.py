#!/usr/bin/python3

with open('input') as f:
    input = f.read().strip().split("\n\n")

def compare(ll,rl):
    while len(rl) > 0:
        rp=rl.pop(0)
        lp=10000
        if len(ll)>0:
            lp = ll.pop(0)
        else:
            return -1
        if type(lp) is list and type(rp) is list:
            r=compare(lp,rp)
            if r != 0:
                return r
        elif type(lp) is int and type(rp) is int:
            if lp < rp:
                return -1
            elif lp > rp:
                return 1
        else:
            if type(lp) is int:
                r=compare([lp],rp)
            else:
                r=compare(lp,[rp])
            if r!=0:
                return r
    if len(ll)>0:
        return 1
    return 0
            

pair=1
p1=0
for p in input:
    l,r=p.split("\n")
    le = eval(l)
    re = eval(r)

    if compare(le,re) < 1:
        p1+=pair

    pair += 1

print("p1",p1)
