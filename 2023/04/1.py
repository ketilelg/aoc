sum=0
sum2=0
with open('sample2') as f:
    cards = f.read().strip().split("\n")

copies=[1]*(len(cards)+1)

for line in cards:
    sum2+=1
    lh,rh=line.split(":")
    cardno=int(lh.split()[1])
    w,c=rh.split("|")
    wins=w.split()
    cards=c.split()
    nwin=len(set(wins).intersection(cards))
    if(nwin>0):
        sum+=2**(nwin-1)
        for i in range(nwin):
            copies[i+cardno+1]+=copies[cardno]
            sum2+=copies[cardno]

print("1:", sum)
print("2:", sum2)
