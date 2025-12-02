import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split(",")

p1=p2=0

def valid(number):
    ss=str(number)
    if len(ss)%2==1: 
        return True   
    return ss[:len(ss)//2]!=ss[len(ss)//2:]

def valid2(number):
    ss=str(number)
    ls=len(ss)
    for i in range(1,ls):
        if ls%i==0 and ss==ss[:i]*(ls//i):
            return False            
    return True

for l in inp:
    start,end=map(int,l.split("-"))
    for i in range(start,end+1):
        if not valid(i):
            p1+=i
        if not valid2(i):
            p2+=i
print("1:",p1)
print("2:",p2)
