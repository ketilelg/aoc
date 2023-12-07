import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    inp = f.read().strip().split("\n")

def hscore(hand):
    #return multiplier based on hand value (16^(rank of hand))
    handa=sorted(hand)
    counts={i:handa.count(i) for i in handa}
    score=1 
    threes=0
    pairs=0
    for v in counts.values():
        if(v==5):
            score=16777216
            break
        elif(v==4):
            score=1048576
            break
        elif(v==3):
            threes+=1
        elif(v==2):
            pairs+=1

        if(threes & pairs):
            score=65536
        elif(threes):
            score=4096
        elif(pairs==2):
            score=256
        elif(pairs==1):
            score=16
    return(score)

game=[]   #tuple: compare value, score, junk
game2=[] #different value calc, with jokers
for i in inp:
    hand,value=i.split()
    hhand="0x"+hand.replace("K","D").replace("Q","C").replace("J","B").replace("A","E").replace("T","A")
    # hhand is now hex string..

    game.append((hscore(hand)*int(hhand,16),value))

    hhand="0x"+hand.replace("K","C").replace("Q","B").replace("J","1").replace("A","D").replace("T","A")
    # test all possible values for joker:

    def hhsc(j):
        return(hscore(hand.replace("J",j)))

    score=max(map(hhsc,["A","K","Q","T","9","8","7","6","5","4","3","2"]))
    game2.append((score*int(hhand,16),value))
            

rank=1
for h in(sorted(game)):
    s1+=rank*int(h[1])
    rank+=1
print("1:", s1)

rank=1
for h in(sorted(game2)):
    s2+=rank*int(h[1])
    rank+=1

print("2:", s2)

