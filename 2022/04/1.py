#!/usr/bin/python3

p1=0
p2=0

with open('input') as f:
    for line in f:
        l1,r1,l2,r2=map(int,line.strip().replace("-",",").split(","))

        if (l1<=l2 and r1>=r2) or (l2<=l1 and r2>=r1):
            p1+=1
        if (l1>=l2 and l1<=r2) or (l2>=l1 and l2<=r1):
            p2+=1

print("p1:",p1)
print("p2:",p2)
