import math
s1=1
s2=0

with open('input') as f:
    inp = f.read().strip().split("\n")

times=list(map(int,inp[0].split(":")[1].split()))
dists=list(map(int,inp[1].split(":")[1].split()))

for (t,d) in zip(times,dists):
    print("t:",t)
    print("d:",d)
    x1=math.floor((-t + math.sqrt((t*t) - (4 * d))) / -2)
    x2=math.ceil((-t - math.sqrt((t*t) - (4 * d))) / -2)
    nn=x2-x1-1
    s1 *= nn
    print("x1",x1,"x2",x2)
    print("n",n,"nn",nn)

    
t=int("".join(list(map(str,times))))
d=int("".join(list(map(str,dists))))

x1=math.floor((-t + math.sqrt((t*t) - (4 * d))) / -2)
x2=math.ceil((-t - math.sqrt((t*t) - (4 * d))) / -2)
s2=x2-x1-1

print("1:", s1)
print("2:", s2)



