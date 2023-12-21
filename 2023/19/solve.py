import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    r,p =  f.read().strip().split("\n\n")


rules={}
for s in r.split("\n"):

    rn,rr=s.split("{")

    rules[rn]=rr[:-1].split(",")

parts=[s[1:-1].split(",") for s in p.split("\n")]


def rulef(rule,x,m,a,s):

    for rr in rules[rule]:

        if(rr.find(":") > 0):
            test,next=rr.split(":")

            if(test.find("<") > 0):
                testval=int(test.split("<")[1])
                if (test.split("<")[0] == "x"):
                    if(x<testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
                if (test.split("<")[0] == "m"):
                    if(m<testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
                if (test.split("<")[0] == "a"):
                    if(a<testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
                if (test.split("<")[0] == "s"):
                    if(s<testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
            if(test.find(">") > 0):
                testval=int(test.split(">")[1])
                if (test.split(">")[0] == "x"):
                    if(x>testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
                if (test.split(">")[0] == "m"):
                    if(m>testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
                if (test.split(">")[0] == "a"):
                    if(a>testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
                if (test.split(">")[0] == "s"):
                    if(s>testval):
                        if(next=="A" or next=="R"):
                            return(next)
                        return(rulef(next,x,m,a,s))
                    
        elif(rr=="A" or rr=="R"):
            return(rr)
        else:
            return(rulef(rr,x,m,a,s))
    print("wtf?")


for p in parts:
    x,m,a,s=map(int,[ i.split("=")[1] for i in p])

    found=False
    if(rulef("in",x,m,a,s)=="A"):
        s1+=x+m+a+s

        
        
    
# print("rules",rules)

print("1:", int(s1))


def overlap(a,b):
    #returns overlap(if any) of (4d) areas a and b
    #area is tuple of tuples (start,end)
    #start,end are tuples: (x,m,a,s)
    nx1=max(a[0][0],b[0][0])
    nx2=min(a[1][0],b[1][0])
    nm1=max(a[0][1],b[0][1])
    nm2=min(a[1][1],b[1][1])
    na1=max(a[0][2],b[0][2])
    na2=min(a[1][2],b[1][2])
    ns1=max(a[0][3],b[0][3])
    ns2=min(a[1][3],b[1][3])
    if((nx2>=nx1) and (nm2>=nm1) and (na2>=na1) and (ns2>=ns1)):
        return(((nx1,nm1,na1,ns1),(nx2,nm2,na2,ns2)))
#    else:
#        return(((0,0,0,0),(0,0,0,0)))
    
def volume(a):
    #return volume of a
    if(a):
        return((1+a[1][0]-a[0][0])*(1+a[1][1]-a[0][1])*
               (1+a[1][2]-a[0][2])*(1+a[1][3]-a[0][3]))
    else:
        return(0)

#demo:



def rulerun(rule,minx,minm,mina,mins,maxx,maxm,maxa,maxs):
    global s2
    #run through rules, build list of areas 
#    print("rulerun",rule,rule,"(",minx,minm,mina,mins,")(",maxx,maxm,maxa,maxs,")")
    mminx=minx
    mmaxx=maxx
    mminm=minm
    mmaxm=maxm
    mmina=mina
    mmaxa=maxa
    mmins=mins
    mmaxs=maxs

    for rr in rules[rule]:
#        print("rrr",rule,rr,"(",mminx,mminm,mmina,mmins,")(",mmaxx,mmaxm,mmaxa,mmaxs,")")
        if(rr.find(":") > 0):
            test,next=rr.split(":")
#            print("t,n",test,next)
            
            if(test.find("<") > 0):
                testval=int(test.split("<")[1])
                if (test.split("<")[0] == "x"):
                    if(maxx>testval):
                        mmaxx=testval-1
                if (test.split("<")[0] == "m"):
                    if(maxm>testval):
                        mmaxm=testval-1
                if (test.split("<")[0] == "a"):
                    if(maxa>testval):
                        mmaxa=testval-1
                if (test.split("<")[0] == "s"):
                    if(maxs>testval):
                        mmaxs=testval-1
            if(test.find(">") > 0):
                testval=int(test.split(">")[1])
                if (test.split(">")[0] == "x"):
                    if(minx<testval):
                        mminx=testval+1
                if (test.split(">")[0] == "m"):
                    if(minm<testval):
                        mminm=testval+1
                if (test.split(">")[0] == "a"):
                    if(mina<testval):
                        mmina=testval+1
                if (test.split(">")[0] == "s"):
                    if(mins<testval):
                        mmins=testval+1
            if(next=="A"):
                s2+=volume(((mminx,mminm,mmina,mmins),(mmaxx,mmaxm,mmaxa,mmaxs)))
            elif(next!="R"):    
                rulerun(next,mminx,mminm,mmina,mmins,mmaxx,mmaxm,mmaxa,mmaxs)
            if(mmaxx!=maxx):
                mminx=mmaxx+1
                mmaxx=maxx
            elif(mminx!=minx):
                mmaxx=mminx-1
                mminx=minx
            if(mmaxm!=maxm):
                mminm=mmaxm+1
                mmaxm=maxm
            elif(mminm!=minm):
                mmaxm=mminm-1
                mminm=minm
            if(mmaxa!=maxa):
                mmina=mmaxa+1
                mmaxa=maxa
            elif(mmina!=mina):
                mmaxa=mmina-1
                mmina=mina
            if(mmaxs!=maxs):
                mmins=mmaxs+1
                mmaxs=maxs
            elif(mmins!=mins):
                mmaxs=mmins-1
                mmins=mins
            
        if ((rr.find(":")<0) and rr!="A" and rr!= "R"):
#            print("DDD")
            rulerun(rr,minx,minm,mina,mins,maxx,maxm,maxa,maxs)
        elif (rr=="A"):
#            print("AAA")
            s2+=volume(((mminx,mminm,mmina,mmins),(mmaxx,mmaxm,mmaxa,mmaxs)))
        minx=mminx
        maxx=mmaxx
        minm=mminm
        maxm=mmaxm
        mina=mmina
        maxa=mmaxa
        mins=mmins
        maxs=mmaxs
            
#        print("rrrend",rule,rr,"(",mminx,mminm,mmina,mmins,")(",mmaxx,mmaxm,mmaxa,mmaxs,")")
        
rulerun("in",1,1,1,1,4000,4000,4000,4000)


print("2:", int(s2))

