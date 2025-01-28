import math
inp=36000000

def get_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factors.update([i, n // i])
    return factors

i=1
r=0
while r<inp:
    r=sum(get_factors(i))*10
    print("i",i,sum(get_factors(i))*10)
    i+=1

print("1:",i-1)

i=1
r=0
while r<inp:
    r=sum(filter(lambda x: x>= i/50,get_factors(i)))*11
    i+=1

print("2:",i-1)