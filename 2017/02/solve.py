import sys
import itertools

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

for l in inp:
    nums=list(map(int,l.split()))
    p1+= max(nums) - min(nums)
    for x,y in itertools.permutations(nums,2):
        if x%y==0:
            p2+=x//y

print("1:",p1)
print("2:",p2)
