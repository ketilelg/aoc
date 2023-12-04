sum1=0

with open('input') as f:
    cards = f.read().strip().split("\n")

copies=[1]*(len(cards)+1)

for line in cards:

    lh,rh=line.split(":")
    cardno=int(lh.split()[1])
    w,c=rh.split("|")
    nwin=len(set(w.split()) & set(c.split()))
    if(nwin>0):
        sum1+=2**(nwin-1)
        for i in range(nwin):
            copies[i+cardno+1]+=copies[cardno]

print("1:", sum1)
print("2:", sum(copies)-1)
