#!/usr/bin/python3

x=y=tx=ty=0
#set of all visited tail positions:
tpos={"0,0"}
tpos9={"0,0"}
#tail arrays, all at start pos..:
tax=[0,0,0,0,0,0,0,0,0]
tay=[0,0,0,0,0,0,0,0,0]
with open('input') as f:
    for line in f:
        h,d=line.strip().split()
        d=int(d)
        if h == "R":
            for i in range(d):
                x+=1
                if (abs(tx-x)>1 and abs(ty-y)>0) or (abs(tx-x)>0 and abs(ty-y)>1): 
                    tx+=int(abs(tx-x)/(x-tx))
                    ty+=int(abs(ty-y)/(y-ty))
                if abs(tx-x)>1:
                    tx+=int(abs(tx-x)/(x-tx))
                if abs(ty-y)>1:
                    ty+=int(abs(ty-y)/(y-ty))
                tay[0]=ty
                tax[0]=tx
                tpos.add(str(tx)+","+str(ty))
                
                for j in range(1,9):

                    if (abs(tax[j]-tax[j-1])>1 and abs(tay[j]-tay[j-1])>0) or (abs(tax[j]-tax[j-1])>0 and abs(tay[j]-tay[j-1])>1): 
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                    if abs(tax[j]-tax[j-1])>1:
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                    if abs(tay[j]-tay[j-1])>1:
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                tpos9.add(str(tax[8])+","+str(tay[8]))
                    
        elif h=="L":
            for i in range(d):
                x-=1
                if (abs(tx-x)>1 and abs(ty-y)>0) or (abs(tx-x)>0 and abs(ty-y)>1): 
                    tx+=int(abs(tx-x)/(x-tx))
                    ty+=int(abs(ty-y)/(y-ty))
                if abs(tx-x)>1:
                    tx+=int(abs(tx-x)/(x-tx))
                if abs(ty-y)>1:
                    ty+=int(abs(ty-y)/(y-ty))
                tay[0]=ty
                tax[0]=tx
                tpos.add(str(tx)+","+str(ty))
                for j in range(1,9):

                    if (abs(tax[j]-tax[j-1])>1 and abs(tay[j]-tay[j-1])>0) or (abs(tax[j]-tax[j-1])>0 and abs(tay[j]-tay[j-1])>1): 
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                    if abs(tax[j]-tax[j-1])>1:
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                    if abs(tay[j]-tay[j-1])>1:
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                tpos9.add(str(tax[8])+","+str(tay[8]))
        elif h=="U":
            for i in range(d):
                y+=1
                if (abs(tx-x)>1 and abs(ty-y)>0) or (abs(tx-x)>0 and abs(ty-y)>1): 
                    tx+=int(abs(tx-x)/(x-tx))
                    ty+=int(abs(ty-y)/(y-ty))
                if abs(tx-x)>1:
                    tx+=int(abs(tx-x)/(x-tx))
                if abs(ty-y)>1:
                    ty+=int(abs(ty-y)/(y-ty))
                tay[0]=ty
                tax[0]=tx
                tpos.add(str(tx)+","+str(ty))
                for j in range(1,9):

                    if (abs(tax[j]-tax[j-1])>1 and abs(tay[j]-tay[j-1])>0) or (abs(tax[j]-tax[j-1])>0 and abs(tay[j]-tay[j-1])>1): 
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                    if abs(tax[j]-tax[j-1])>1:
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                    if abs(tay[j]-tay[j-1])>1:
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                tpos9.add(str(tax[8])+","+str(tay[8]))
        elif h=="D":
            for i in range(d):
                y-=1
                if (abs(tx-x)>1 and abs(ty-y)>0) or (abs(tx-x)>0 and abs(ty-y)>1): 
                    tx+=int(abs(tx-x)/(x-tx))
                    ty+=int(abs(ty-y)/(y-ty))
                if abs(tx-x)>1:
                    tx+=int(abs(tx-x)/(x-tx))
                if abs(ty-y)>1:
                    ty+=int(abs(ty-y)/(y-ty))
                tay[0]=ty
                tax[0]=tx
                tpos.add(str(tx)+","+str(ty))
                for j in range(1,9):

                    if (abs(tax[j]-tax[j-1])>1 and abs(tay[j]-tay[j-1])>0) or (abs(tax[j]-tax[j-1])>0 and abs(tay[j]-tay[j-1])>1): 
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                    if abs(tax[j]-tax[j-1])>1:
                        tax[j]+=int(abs(tax[j]-tax[j-1])/(tax[j-1]-tax[j]))
                    if abs(tay[j]-tay[j-1])>1:
                        tay[j]+=int(abs(tay[j]-tay[j-1])/(tay[j-1]-tay[j]))
                tpos9.add(str(tax[8])+","+str(tay[8]))
        else:
            print("huh",h)

print("p1",len(tpos))
print("p2",len(tpos9))
            
    
