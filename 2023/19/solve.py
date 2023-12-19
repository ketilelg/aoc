import math
import sys

s1=0
s2=0

with open(sys.argv[1] if (len(sys.argv) == 2) else 'sample') as f:
    r,p =  f.read().strip().split("\n\n")


rules={}
for s in r.split("\n"):
#    print("s",s)
    rn,rr=s.split("{")
    print("rnr",rn,"rr",rr)
    rules[rn]=rr[:-1].split(",")

parts=[s[1:-1].split(",") for s in p.split("\n")]


def rulef(rule,x,m,a,s):
    print("rulef",rule,x,m,a,s)
    for rr in rules[rule]:
        print("rfrr",rr)
        if(rr.find(":") > 0):
            test,next=rr.split(":")
            print("test",test,next)
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
                    print("tests",s,testval,next)
                    if(s<testval):
                        print("less")
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

        
        
    
print("rules",rules)

print("1:", int(s1))


print("2:", int(s2))

