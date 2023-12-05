s1=0
s2=0

with open('input') as f:
    inp = f.read().strip().split("\n\n")



for i in inp:
    print("i:",i)

    if (i.find("seeds:") == 0):
        seeds=i.split(":")[1].split()
        print("seeds",seeds)
    else:
        m=i.split(":\n")[1].split("\n")
        print("m:",m)
        ns=[]
        for s in seeds:
            print("fs",s)
            np=-1
            for fm in m:
                ff=fm.split()
                print("ff",ff,"s",s)
                if((int(s) >= int(ff[1])) & (int(s) < (int(ff[1])+int(ff[2])))):
                    np=int(s)-(int(ff[1])-int(ff[0]))
                    print("yy",np)
            if(np<0):
                np=int(s)
            ns.append(np)
        print("ns:",ns)
        seeds=ns
seeds.sort()
print("sorted",seeds)
print("1:", seeds[0])
print("2:", s2)
