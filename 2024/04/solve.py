import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    map = list(map(list,f.read().strip().split("\n")))

p1=0
p2=0

w=len(map)
h=len(map[0])

for y in range(len(map)):
    for x in range(len(map[0])):
        if(map[y][x]=="X"):
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    if ((0<= x+dx*3 < w)
                        and (0 <= y+dy*3 < h)
                        and (map[y+dy*1][x+dx*1]+
                             map[y+dy*2][x+dx*2]+
                             map[y+dy*3][x+dx*3] == "MAS")):
                        p1+=1

    
for x in range(1,len(map[0])-1):
    for y in range(1,len(map)-1):
        if(map[y][x]=="A"):
            if (((map[y-1][x-1]=="M" and map[y+1][x+1]=="S") or
                 (map[y-1][x-1]=="S" and map[y+1][x+1]=="M")) and
                ((map[y+1][x-1]=="M" and map[y-1][x+1]=="S") or
                 (map[y+1][x-1]=="S" and map[y-1][x+1]=="M"))):
                p2+=1


print("1:",p1)
print("2:",p2)
