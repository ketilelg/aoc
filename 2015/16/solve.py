import sys
from collections import defaultdict
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0


pack={"children": 3,"cats": "7",
"samoyeds": "2",
"pomeranians": "3",
"akitas": "0",
"vizslas": "0",
"goldfish": "5",
"trees": "3",
"cars": "2",
"perfumes": "1"}


for b in inp:
    sue,an1,ann1,an2,ann2,an3,ann3=re.findall(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)",b)[0]
    ls=b.split(":")
    ts={an1:ann1,an2:ann2,an3:ann3}
#    print("lls",an1,an2,an3)  
    if pack[an1]==ann1 and pack[an2]==ann2 and pack[an3]==ann3:
        print("sue",sue)
        p1=sue
    np2=0
    for t in ts:
        if t=="cats" or t=="trees":
            if int(ts[t]) > int(pack[t]):
                np2+=1
        elif t=="pomeranians" or t=="goldfish":
            if int(ts[t]) < int(pack[t]):
                np2+=1
        else:
            if ts[t]==pack[t]:
                np2+=1
    if np2==3:
        print("sue2",sue)
        p2=sue
print("1:",p1) 
print("2:",p2)
