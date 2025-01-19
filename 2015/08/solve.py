import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


for b in inp:
#    print("b",b)
    strl=len(b)
    bl=list(b)
    nstr=""
    c=bl.pop(0)
    p2l=0
    while bl:
        print("bl",bl,c)
        if c=="\\":
            nxt=bl.pop(0)
            if nxt=="x":
                ch=bl.pop(0)+bl.pop(0)
                nstr+="!"
                p2l+=5
            elif nxt=="\\":
                nstr+="\\"
                p2l+=4
            elif nxt=='"':
                nstr+='"'
                p2l+=4
        elif c=='"':
            nstr+=""
            p2l+=3
        else:
            nstr+=c
            p2l+=1
        print("sdfsdf",c,bl,p2l)
        if bl:
            c=bl.pop(0)
#    print("nstr",nstr)
    p2l+=3
    p1+=(strl-len(nstr))
    p2+=p2l-strl
    print("bbb",p2l,strl,b)
    
print("1:",p1)
print("2:",p2)
