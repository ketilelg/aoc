#!/usr/bin/python3

def solve(n,s):
   for i in range(len(s)-n):
       if len(set(s[i:i+n]))==n:
           return i+n

with open('input') as f:
    for line in f:
        print("res4:",solve(4,line.strip()))
        print("res14:",solve(14,line.strip()))



