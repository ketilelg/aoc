import math

with open('input') as f:
    inp = f.read().strip().split("\n")

times=list(map(int,inp[0].split(":")[1].split()))
dists=list(map(int,inp[1].split(":")[1].split()))

s1=1

def ntimes(t,d):
    x1=math.ceil((-t + math.sqrt((t*t) - (4 * d))) / -2)
    x2=math.floor((-t - math.sqrt((t*t) - (4 * d))) / -2)
    return(x2-x1+1)
    

for (t,d) in zip(times,dists):
    s1 *= ntimes(t,d)

print("1:", s1)
        
t=int("".join(list(map(str,times))))
d=int("".join(list(map(str,dists))))

print("2:", ntimes(t,d))



