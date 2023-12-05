s1=0
s2=0

with open('input') as f:
#with open('sample') as f:
    inp = f.read().strip().split("\n\n")



for i in inp:
#    print("i:",i)

    if (i.find("seeds:") == 0):
        seeds=list(map(int,i.split(":")[1].split()))
#        print("seeds",seeds)
        seeds2=seeds
        it=iter(seeds2)
        seeds2=[(x, next(it)) for x in it ]
#        print("s2:",seeds2)
    else:
        m=i.split(":\n")[1].split("\n")
#        print("m:",m)
        ns=[]
        for s in seeds:
#            print("fs",s)
            np=-1
            for fm in m:
                ff=list(map(int,fm.split()))
#                print("ff",ff,"s",s)
                if((s >= ff[1]) & (s < (ff[1]+ff[2]))):
                    np=s-(ff[1]-ff[0])
#                    print("yy",np)
            if(np<0):
                np=s
            ns.append(np)
#        print("ns:",ns)
        seeds=ns
        s2r=[] #remapped
        for fm in m:
            ff=list(map(int,fm.split()))
#            print("ff",ff,"seeds2",seeds2)
            s2n=[] #non-remapped
            for s2 in seeds2:
#                print("s2",s2)
                if ((s2[0] >= ff[1]) & (s2[0] < (ff[1]+ff[2])) &
                    ((s2[0] + s2[1]) <= (ff[1] + ff[2]))):
#                    print("xx all inside")
                    s2r.append((s2[0]-(ff[1]-ff[0]),s2[1]))
#                    print(":",s2r,s2n)
                elif ((s2[0] >= (ff[1]+ff[2])) | ((s2[0]+s2[1]) < ff[1])):
#                    print("xx all outside")
                    s2n.append(s2)
#                    print(":",s2r,s2n)
                elif ((s2[0] < ff[1]) & ((s2[0] + s2[1]) >= (ff[1] + ff[2]))):
#                    print("xx bigger lr")
                    s2n.append((s2[0],ff[1]-s2[0]))
                    s2r.append((ff[1],ff[2]))
                    s2n.append((ff[1]+ff[2],(s2[0]+s2[1])-(ff[1]+ff[2])))
#                    print(":",s2r,s2n)
                elif ((s2[0] < ff[1]) & ((s2[0] + s2[1]) < (ff[1] + ff[2]))):
#                    print("xx overlap l")
                    s2n.append((s2[0],ff[1]-s2[0]))
                    s2r.append((ff[0],(s2[0]+s2[1])-(ff[1])))
#                    print(":",s2r,s2n)
                elif ((s2[0] >= ff[1]) & ((s2[0] + s2[1]) >= (ff[1] + ff[2]))):
#                    print("xx overlap r")
                    s2r.append((s2[0]-(ff[1]-ff[0]),(ff[1]+ff[2])-s2[0]))
                    s2n.append((ff[1]+ff[2],(s2[0]+s2[1])-(ff[1]+ff[2])))
#                    print(":",s2r,s2n)
#                else:
#                    print("wtf???")
                
            seeds2=s2n #only check non-remapped seeds next round

#            print("s2n",s2n,"s2r",s2r)
        seeds2=s2n+s2r
#        print("seeds2",seeds2,"\n\n")

       
seeds.sort()
seeds2.sort()

print("1:", seeds[0])
print("2:", seeds2[0][0])
