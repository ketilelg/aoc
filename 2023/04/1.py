sum=0
sum2=0
with open('input') as f:
    cards = f.read().strip().split("\n")

copies=[1]*(len(cards)+1)

for line in cards:
    sum2+=1
    lh,rh=line.split(":")
    cardno=int(lh.split()[1])
    w,c=rh.split("|")
    wins=w.split()
    cards=c.split()
    nwin=0
    for ww in wins:
        if(ww in cards):
            nwin+=1
    if(nwin>0):
        sum+=2**(nwin-1)
        for i in range(nwin):
            copies[i+cardno+1]+=copies[cardno]
            sum2+=copies[cardno]

print("1:", sum)
print("2:", sum2)
