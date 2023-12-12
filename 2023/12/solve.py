import math
import sys

s1=0
s2=0

sys.setrecursionlimit(100000)

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    lines = ((s.split(" ")) for s in  f.read().strip().split("\n"))


def repl(ss,ds,pos):
    str=ss
    m=0

    
    if(pos< len(str)):

        if(str[pos]=="?"):

            for r in ".#":
                nstr=str.replace("?",r,1)
                lc =(list(map(len,(g for g in str[:pos].split(".") if (g)))))
#                print("lcds",lc,ds,nstr)
                if(lc[:max(0,len(lc)-1)]==ds[:max(0,len(lc)-1)]):
                    m+=repl(nstr,ds,pos+1)
#                else:
#                    print("cut")
        else:
            m+=repl(str,ds,pos+1)
    else:
        lc =(list(map(len,(g for g in str[:pos].split(".") if (g)))))
#        print("str",str)
        
        # matcher lista med tallene?
#        print("lc",lc,ds)
        if(lc==ds):
#            print("match",str)
            m=1
        else:
            m=0
    return(m)



for l in lines:
    print()
    print("L",l)

    ds=(list(map(int,l[1].split(","))))
    r=repl(l[0],ds,0)
#    print("res",r)
#    gjør noe ala "test for med #/. foran/bak, multipliser resultatene.
#    (.) skiller, så no problem, # kan koples til foran og/eller bak,
#    må tenkes


#    l2=l[0]+"?"+l[0]+"?"+l[0]+"?"+l[0]+"?"+l[0]
#    ds2=ds*5
#    print("l2ds2",l2,ds2)
#    r2=repl(l2,ds2,0)
#    print("res2",r2)
#    s2+=r2


    s1+=r

                    
        
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

