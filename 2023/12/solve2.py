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
        
        # matcher lista med tallene?
#        print("lc",lc,ds)
        if(lc==ds):
#            print("match",str)
            m=1
        else:
            m=0
#        print("str",str,m)

    return(m)



def p2r(l,ds,p2,p):
    r=0
    if(p<len(p2)):
        for c in [".l",".r","#l","#r"]:
            p2[p]=c
            r+=p2r(l,ds,p2,p+1)
        return(r)
    else:
        print("p2",p2)
        m=1
        n=1
        pr=""
        for p,c in enumerate(p2):
            print("cp",c[0],c[1],pr)
            if(c[1]=="l"):
                m1=repl(pr+l+c[0],ds,0)
                pr=""
            else:
                m1=repl(pr+l+l[-1],ds,0)
                pr=c[0]

            print("cpe",m1,pr)
            m=m*m1
            pstr="".join([x[0] for x in p2])
#            print("pstr",pstr)
        m=m*repl(pr+l,ds,0)
        if(pstr in p2ass):
            p2ass[pstr]=p2ass[pstr]+","+str(m)
        else:
            p2ass[pstr]=str(m)                
        print("m",m,p2)
        return(m)


# 1 2 3 4 5
# 1 l 2 l 3 l 4 l 5
# 1l 2l 3l 4l 5


for l in lines:
    print()
    print("L",l)

    ds=(list(map(int,l[1].split(","))))
    r=repl(l[0],ds,0)
    print("res",r)
    print("-.",repl(l[0]+".",ds,0))
    print("-#",repl(l[0]+"#",ds,0))
    print()
    print("..",repl("."+l[0]+".",ds,0))
    print(".#",repl("."+l[0]+"#",ds,0))
    print("#.",repl("#"+l[0]+".",ds,0))
    print("##",repl("#"+l[0]+"#",ds,0))
    print()
    print(".-",repl("."+l[0],ds,0))
    print("#-",repl("#"+l[0],ds,0))
    p2ass={}
#    print("p2r",p2r(l[0],ds,[".l",".l",".l",".l"],0))
#    print("p2ass",p2ass)
    
#    gjør noe ala "test for med #/. foran/bak, multipliser resultatene.
#    (.) skiller, så no problem, # kan koples til foran og/eller bak,
#    må tenkes

# hvis start&slutt!= .: faktor 1.
# hvis start&slutt= .: (opprinnelig verdi)**5 (for 5 repeats) * 2**4 (for de nye, som ikke har verdi)
# 
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

