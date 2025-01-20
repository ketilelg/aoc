import sys
import re
import json

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=p2=0

finds=re.findall(r"(-?\d+)",inp)
for i in finds:
#    print("ff",i)
    p1+=int(i)



def dumpj(jj):
    global p2
    if type(jj) is dict:
        print("\n\ndict",jj.keys(),jj.values())
        if not "red" in jj.values():
            for j in jj.values():
                dumpj(j) 
        else:
            print("\n\nRED\n\n")
    elif type(jj) is list:            
        print("list")
        for j in jj:
            dumpj(j) 

    else:
        print("\n\nSOLO",jj,type(jj))
        if type(jj) is int:
            p2+=jj




jj=json.loads(inp)

dumpj(jj)

print("1:",p1)
print("2:",p2)
