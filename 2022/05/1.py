#!/usr/bin/python3

p1=0
p2=0
c = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
with open('input') as f:
    for line in f:
        if line.find("]")>0:
            for x in range(0,len(line)-1,4):
                s=int(x/4)
                cc=line[x:x+3]
                if cc.find("]")>0:
#                print(s,x,'"',line[x:x+3],'"')
                    c[s].insert(0,line[x:x+3])
#                print(len(line),line)

        elif line.find("from")>0:
            x,n,xx,f,xxx,t=line.split()
            print("nft",n,f,t)
            for i in range(0,int(n)):
                print("move",i,f,t)
                c[int(t)-1].append(c[int(f)-1].pop())
            for i in c:
                print(i)




for i in c:
    if i:
        print(i.pop())

    
