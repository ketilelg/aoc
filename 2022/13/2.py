#!/usr/bin/python3

import functools
input=[]
with open('input') as f:
    for line in f:
        x=line.strip()
        if x:
            input.append(x)
            
input.append("[[2]]")
input.append("[[6]]")


def compare(lli,rli):
    if type(lli) is str:
        ll=eval(lli)
    else:
        ll=lli.copy()
    if type(rli) is str:
        rl=eval(rli)
    else:
        rl=rli.copy()
        
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
            
sorted_input=sorted(input,key=functools.cmp_to_key(compare))

print("p2",(sorted_input.index("[[2]]")+1) * (sorted_input.index("[[6]]")+1))

