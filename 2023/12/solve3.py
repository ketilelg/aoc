import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    lines = ((s.split(" ")) for s in  f.read().strip().split("\n"))

def repl(rec,li,pos):
    #rec = record, li=list, pos=startpos (trengs denne?)
    done=False
    nhash=0
    chash=0
    nq=0
    last=" "
    while(pos < len(rec)):
        if(rec[pos]==".":
           last=rec[pos]
           pos+=1
           nq=0
           nhash=0
           # regne på den bolken vi har, fra start til pos. spis så mange fra lista som det går..
        elif(rec[pos]=="#":
             nhash+=1
             if(last=="#":
                chash+=1
             pos+=1
             # count number of hashes
        elif(rec[pos]=="?":
             nq+=1
             pos+=1
             # count number of ?
        else:
             print("wtf?",

for l in lines:
    print()
    print("L",l)

    ds=(list(map(int,l[1].split(","))))
    r=repl(l[0],ds,0)
    s1+=r

                    
        


                
          
        
          

print("1:", int(s1))

print("2:", int(s2))

