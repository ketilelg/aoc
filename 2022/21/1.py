#!/usr/bin/python3

import re
from sympy import symbols,solve

monkeys={}
rev={}
f=open('sample')
for l in f.read().strip().split("\n"):
    monkey,value=l.split(": ")
    monkeys[monkey]=value
    if not re.search("\d+",value):
        l,op,r=value.split(" ")
        rev[l]=monkey
        rev[r]=monkey
        

def findvalue(monkey):
    v = re.search("\d+",monkeys[monkey])
    if v:
        return int(monkeys[monkey])
    else:
        l,op,r=monkeys[monkey].split(" ")
        if op == "+":
            return findvalue(l) + findvalue(r)
        if op == "-":
            return findvalue(l) - findvalue(r)
        if op == "*":
            return findvalue(l) * findvalue(r)
        if op == "/":
            return findvalue(l) / findvalue(r)

def findeq(monkey):
    if monkey=="humn":
        return " h "
    v = re.search("\d+",monkeys[monkey])
    if v:
        return monkeys[monkey]
    else:
        l,op,r=monkeys[monkey].split(" ")
        if monkey=="root":
            return findeq(l) + " - " + findeq(r)
        if op == "+":
            return "(" + findeq(l) + " + " + findeq(r) + ")"
        if op == "-":
            return "(" + findeq(l) + " - " + findeq(r) + ")"
        if op == "*":
            return "(" + findeq(l) + " * " + findeq(r) + ")"
        if op == "/":
            return "(" + findeq(l) + " / " + findeq(r) + ")"

        
print("p1:",findvalue("root"))

eq=findeq("root")

# print("eq",eq)

h=symbols('h')
sol=solve(eq)

print("p2:",sol[0])
