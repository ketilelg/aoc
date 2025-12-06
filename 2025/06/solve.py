import sys
import numpy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().split("\n")

p1=p2=0

inp.pop()

sheet=[]
for l in inp[:-1]:
    sheet.append(list(map(int,l.split())))
sheet.append(inp[-1].split())

for i in range(len(sheet[0])):
    v=sheet[0][i]
    op=sheet[-1][i]
    for j in range(1,len(sheet)-1):
        if op=="+":
            v+=sheet[j][i]
        else: #op=="*"
            v*=sheet[j][i]
    p1+=v

#del 2. se på tabellen som chars, slice den nedover
sh2=numpy.array(list(list(x) for x in inp))

sv=0
op=""
for i in range(len(sh2[0])):
    ss=sh2[0:len(sh2),i]
    if "".join(ss[:-1]).strip() != "":
        v=int("".join(ss[:-1]))
        if ss[-1]!=" ":
            op=ss[-1]
            p2+=sv
            if op=="+":
                sv=0
            else:
                sv=1
        if op=="+":
            sv+=v
        else:
            sv*=v
p2+=sv

print("1:",p1)
print("2:",p2)
