#!/usr/bin/python3

p1=0
p2=0

with open('input') as f:
    for line in f:
        l,r=line.strip().split(",")
        l1,r1=l.split("-")
        l2,r2=r.split("-")
        print(l1,r1,l2,r2)
        if (int(l1)<=int(l2) and int(r1)>=int(r2)) or (int(l2)<=int(l1)) and (int(r2)>=int(r1)):
            print("over")
            p1+=1
        if (int(l1)>=int(l2) and int(l1)<=int(r2)) or (int(l2)>=int(l1)) and (int(l2)<=int(r1)):
            print("sover")
            p2+=1




print("p1:",p1)
print("p2:",p2)
