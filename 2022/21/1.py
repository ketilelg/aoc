#!/usr/bin/python3
import re
from sympy import solve

monkeys=dict(l.split(": ") for l in open("input").read().strip().split("\n"))
        
def findeq(monkey):
    if re.search("\w+ \W \w+",monkeys[monkey]):
        l,op,r=monkeys[monkey].split(" ")
        return "(" + findeq(l) + op + findeq(r) + ")"
    else:
        return monkeys[monkey]


print("p1",int(eval(findeq("root"))))
monkeys["root"] = monkeys["root"].replace("+","-")
monkeys["humn"] = " h "
print("p2:",solve(findeq("root"))[0])
