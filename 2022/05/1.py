#!/usr/bin/python3

c = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
with open('input') as f:
    for line in f:
        if line.find("]")>0:
            for x in range(0,len(line)-1,4):
                s=int(x/4)
                cc=line[x:x+3]
                if cc.find("]")>0:
                    c[s].insert(0,line[x:x+3])
        elif line.find("from")>0:
            x,n,xx,f,xxx,t=line.split()
            for i in range(0,int(n)):
                c[int(t)-1].append(c[int(f)-1].pop())
for i in c:
    if i:
        print(i.pop())

    
