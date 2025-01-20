import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=0
p2=0

alph="abcdefghjkmnpqrstuvwxyz"

def incr(pws):
    def cinc(c):
        carry=False
        p=alph.find(c)
        np=p+1
#        print("cinc",c,np)
        if np==len(alph):
            np=0    
            carry=True
        return alph[np],carry

    pw=list(pws)
    nc,carry=cinc(pw[-1])
    pw[-1]=nc
    p=-1
    while carry:
        p-=1
        nc,carry=cinc(pw[p])
        pw[p]=nc
    return "".join(pw)

def pwok(pw):
    ok=False
    i=0
    while not ok and i<len(pw)-3:
        ok= (alph.find(pw[i])+1==alph.find(pw[i+1])) and (alph.find(pw[i+1])+1==alph.find(pw[i+2]))
#        print("ttt",alph.find(pw[i]),alph.find(pw[i+1]),alph.find(pw[i+2]),ok)
        i+=1
    if ok:
        p="-"
        pairs=0
        for c in pw:
#            print("pwok",pw,c,p,pairs)
            if p==c:
                pairs+=1
                p="-"
            else:
                p=c
        return pairs>1
    return False

pw=inp
while not pwok(pw):
    pw=incr(pw)
#    print("sdf",pw)
print("1:",pw)
pw=incr(pw)
while not pwok(pw):
    pw=incr(pw)
print("2:",pw)
