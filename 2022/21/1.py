#!/usr/bin/python3
import re
from sympy import solve

monkeys=dict(l.split(": ") for l in open("sample").read().strip().split("\n"))
        
def findeq(monkey):
    if monkey=="humn":
        return " h "
    if re.search("\d+",monkeys[monkey]):
        return monkeys[monkey]
    else:
        l,op,r=monkeys[monkey].split(" ")
        return "(" + findeq(l) + op + findeq(r) + ")"

h=int(monkeys["humn"])
print("p1",int(eval(findeq("root"))))
monkeys["root"]= monkeys["root"].replace("+","-")
print("p2:",solve(findeq("root"))[0])
