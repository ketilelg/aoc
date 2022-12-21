#!/usr/bin/python3
import re
from sympy import symbols,solve

monkeys={}
f=open('input')
for l in f.read().strip().split("\n"):
    monkey,value=l.split(": ")
    monkeys[monkey]=value
        
def findeq(monkey):
    if monkey=="humn":
        return " h "
    v = re.search("\d+",monkeys[monkey])
    if v:
        return monkeys[monkey]
    else:
        l,op,r=monkeys[monkey].split(" ")
        return "(" + findeq(l) + op + findeq(r) + ")"

h=int(monkeys["humn"])
print("p1",int(eval(findeq("root"))))
monkeys["root"]= monkeys["root"].replace("+","-")
h=symbols('h')
print("p2:",solve(findeq("root"))[0])
