import sys
import re

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=0
p2=0

do=True
matches=re.findall(r"((mul)\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))",inp)
for x in matches:
    if(x[1] == "mul"):
        p1+=int(x[2])*int(x[3])
        if do:
            p2+=int(x[2])*int(x[3])
    else:
        do = x[4] == "do()"

print("1:",p1)
print("2:",p2)
