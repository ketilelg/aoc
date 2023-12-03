import re
sum=0
sum2=0
with open('input') as f:
    engine = f.read().strip().split("\n")
w=len(engine[0])
h=len(engine)
lineno=0
m=re.compile("\d+") #find numbers
s=re.compile("[^0-9.]") #find symbols
g=re.compile("[*]") #find multiplication
for line in engine:
    print("line:",line)
    for f in m.finditer(line):
        for sline in engine[max(0,lineno-1) : min(h,lineno+2)]:
            substr=sline[max(f.start()-1,0):min(f.end()+1,w)]
            sl=s.finditer(substr)
            for ss in sl:
                sum+=int(f.group())
    for gg in g.finditer(line):
        print("gg",gg)
        flist= []
        for sline in engine[max(0,lineno-1) : min(h,lineno+2)]:
            for ff in m.finditer(sline):
                if((gg.start() <= ff.end() ) & (gg.end() >= ff.start())):
                    flist.append(int(ff.group()))
        print("fl",flist)
        if(len(flist) == 2):
            v=flist[0]*flist[1]
            sum2+=v
    lineno+=1
print("1:", sum)
print("2:", sum2)
