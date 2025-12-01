import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

def abba(str):
    return str[0]==str[3] and str[1]==str[2] and str[0]!=str[1]

for k in inp:
    print("k",k)
    print("kk",re.split("\[|\]",k))
    blev=0
    abbain=False
    abbaout=False
    for c in range(len(k)-3):
        subs=k[c:c+4]
        match k[c]:
            case "[":
                blev+=1
            case "]":
                blev-=1
        if abba(subs):
            if blev==0:
                abbaout=True
            else:
                abbain=True
        print("dd",subs,abba(subs),blev,abbain,abbaout)
    if abbaout and not abbain:
        p1+=1

print("1:",p1)
print("2:",p2)
