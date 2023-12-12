import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    lines = ((s.split(" ")) for s in  f.read().strip().split("\n"))


def br(dds,ggg,c):
    ds=dds
    gg=ggg
    print("br",ds,gg)

    # matcher lista med tallene?
    lc =(list(map(len,gg)))
    print("lc",lc,ds)
    if(lc==ds):
        print("match")
        return 1

    
    if(gg[0].find("?") >=0):
        print("q")
        # iterer over alle mulige gg[0]:
        
        
    else:
        print("hash")
        return(br(ds[1:],gg[1:],c))
       
       
#    for g in gg:
#        print("g",g)
#        if(g.find("?") >= 0):
#            print("q")
#            for 
#        else:
#            print("hash",g,l)
#            if(
    return 0

def repl(str,ds,pos):
    m=0
    if(pos< len(str)):
        if(str[pos]=="?"):
            for r in ".#":
                m+=repl(str.replace("?",r,1),ds,pos+1)
        else:
            m+=repl(str,ds,pos+1)
    else:
#        print("str",str)
        
        # matcher lista med tallene?
        lc =(list(map(len,(g for g in str.split(".") if (g)))))
#        print("lc",lc,ds)
        if(lc==ds):
#            print("match")
            m=1
        else:
            m=0
    return(m)


for l in lines:
#    print()
#    print("L",l)

    ds=(list(map(int,l[1].split(","))))
    s1+=repl(l[0],ds,0)
    print("result:",s1)
        
#    gg=[g for g in l[0].split(".") if(g)]
#    br(ds,gg,0)
#    for g in gg:
#        print("g",g)
#        if(g.find("?") >= 0):
#            print("q")
#        else:
#            print("hash")


                
          
        
          

print("1:", int(s1))

print("2:", int(s2))

