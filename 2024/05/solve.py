import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    f1,f2 = f.read().strip().split("\n\n")

order=f1.split("\n")
prod=f2.split("\n")

p1=0
p2=0

def before(p1,p2):
    res=True
    for t in order:
        l,r=t.split("|")
        if(l==p1 and  r==p2):
            return True
        elif (r==p1 and l==p2):
            return False

def inorder(pp):
    ordered=True
    for i in range(len(pp)-1):
        ordered=ordered and before(pp[i],pp[i+1])
    return ordered

for p in prod:
    pp=p.split(",")
    if inorder(pp):
        p1+=int(pp[int(len(pp)/2)])
    else:
        while not inorder(pp): #bubblesort for the win
            for i in range(len(pp)-1):
                if not before(pp[i],pp[i+1]):
                    pp[i],pp[i+1] = pp[i+1],pp[i]
        p2+=int(pp[int(len(pp)/2)])

print("1:",p1)
print("2:",p2)
