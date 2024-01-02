import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    stones = [list(map(int,s.replace("@",",").split(","))) for s in f.read().strip().split("\n")]


print("stones",stones)

for i,stone1 in enumerate(stones):
    print("loop",i,stone1)
    for stone2 in stones[i+1:]:
        print("inner",stone2)

print("1:", s1)
    
print("2:", s2)

